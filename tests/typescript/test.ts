import { join } from "path";
import {
    readdirSync,
    readFileSync,
    lstatSync,
    existsSync,
    writeFileSync,
} from "fs";
import { strict } from "assert";
import { describe, it } from "mocha";
import { Context } from "./dependencies";

const minify = (json: any) => {
    var tokenizer = /"|(\/\*)|(\*\/)|(\/\/)|\n|\r/g,
        in_string = false,
        in_multiline_comment = false,
        in_singleline_comment = false,
        tmp,
        tmp2,
        new_str = [],
        ns = 0,
        from = 0,
        lc,
        rc;

    tokenizer.lastIndex = 0;

    while ((tmp = tokenizer.exec(json))) {
        // @ts-ignore
        lc = RegExp.leftContext;
        // @ts-ignore
        rc = RegExp.rightContext;
        if (!in_multiline_comment && !in_singleline_comment) {
            tmp2 = lc.substring(from);
            if (!in_string) {
                tmp2 = tmp2.replace(/(\n|\r|\s)*/g, "");
            }
            new_str[ns++] = tmp2;
        }
        from = tokenizer.lastIndex;

        if (tmp[0] == '"' && !in_multiline_comment && !in_singleline_comment) {
            tmp2 = lc.match(/(\\)*$/);
            if (!in_string || !tmp2 || tmp2[0].length % 2 == 0) {
                // start of string with ", or unescaped " character found to end string
                in_string = !in_string;
            }
            from--; // include " character in next catch
            rc = json.substring(from);
        } else if (
            tmp[0] == "/*" &&
            !in_string &&
            !in_multiline_comment &&
            !in_singleline_comment
        ) {
            in_multiline_comment = true;
        } else if (
            tmp[0] == "*/" &&
            !in_string &&
            in_multiline_comment &&
            !in_singleline_comment
        ) {
            in_multiline_comment = false;
        } else if (
            tmp[0] == "//" &&
            !in_string &&
            !in_multiline_comment &&
            !in_singleline_comment
        ) {
            in_singleline_comment = true;
        } else if (
            (tmp[0] == "\n" || tmp[0] == "\r") &&
            !in_string &&
            !in_multiline_comment &&
            in_singleline_comment
        ) {
            in_singleline_comment = false;
        } else if (
            !in_multiline_comment &&
            !in_singleline_comment &&
            !/\n|\r|\s/.test(tmp[0])
        ) {
            new_str[ns++] = tmp[0];
        }
    }
    new_str[ns++] = rc;
    return new_str.join("");
};

const ROOT_DIR = join("../../");
const SPECIFICATION_FILE = join(ROOT_DIR, "spec.jsonc");
const LANG_DIR = join(ROOT_DIR, "lang/");
const TEMP_FILE = "tmp_logic.ts";

const getLanguageSpecification = (): {
    version: number;
    groups: string[];
} => JSON.parse(minify(readFileSync(SPECIFICATION_FILE, "utf-8")));

const getGroupFunctions = (groupName: string): string[] => {
    const GROUP_FOLDER = join(LANG_DIR, `${groupName}/`);
    const functions: string[] = [];
    readdirSync(GROUP_FOLDER).forEach((file: string) => {
        if (lstatSync(join(GROUP_FOLDER, file)).isDirectory()) {
            functions.push(file);
        }
    });
    return functions;
};

console.log("Running Typescript Tests");

console.log("Building Temp file");

// Get the language specification
const languageSpecification = getLanguageSpecification();
// First part of the tmp file
let tempFileContent = `import { Context, Node, PrimativeTypes } from "./dependencies";\n`;

for (const group of languageSpecification.groups) {
    const groupFunctions = getGroupFunctions(group);
    for (const funcName of groupFunctions) {
        const funcDir = join(LANG_DIR, `${group}/`, `${funcName}/`);
        const funcLogicFile = join(funcDir, "logic.ts");
        if (existsSync(funcLogicFile)) {
            const funcLogic = readFileSync(funcLogicFile, "utf-8").replace(
                "const logic ",
                `const ${funcName.toLowerCase()}_logic`,
            );
            tempFileContent += `${funcLogic}\n`;
        }
    }
}

writeFileSync(TEMP_FILE, tempFileContent);

const logicFunctions = require("./tmp_logic");

let log: string = "";
const mockCtx = new Context(
    {
        foo_1: "bar",
    },
    {
        logFunc: (value: any) => {
            log += value + "\n";
        },
    },
);

describe("Typescript Functions", () => {
    for (const group of languageSpecification.groups) {
        describe(group, () => {
            const groupFunctions = getGroupFunctions(group);
            for (const funcName of groupFunctions) {
                describe(funcName, () => {
                    const funcDir = join(LANG_DIR, `${group}/`, `${funcName}/`);
                    const funcSpecFile = join(funcDir, "spec.jsonc");
                    const funcSpec = JSON.parse(
                        minify(readFileSync(funcSpecFile, "utf-8")),
                    );

                    const logicFunc =
                        logicFunctions[`${funcName.toLowerCase()}_logic`];

                    const testSpec = funcSpec[1].tests;

                    if (typeof testSpec == "undefined") {
                        console.warn(`No tests specified for ${funcName}`);
                    } else {
                        for (const i in testSpec) {
                            it(`Test #${parseInt(i) + 1}`, () => {
                                const [_, testAttr] = testSpec[i];
                                const args = testAttr.arguments;
                                const returns = testAttr.returns;
                                const createdSymbols =
                                    testAttr.createdSymbols || [];
                                const inLog = testAttr.inLog || null;

                                let actual = logicFunc(mockCtx, ...args);
                                if (typeof actual == "undefined") actual = null;

                                if (Array.isArray(returns)) {
                                    strict.deepStrictEqual(actual, returns);
                                } else {
                                    strict.strictEqual(actual, returns);
                                }
                                // Check for values in the log.
                                if (inLog != null) {
                                    strict.ok(log.includes(inLog));
                                }

                                // Check for created symbols.
                                for (const createdSymbol of createdSymbols) {
                                    const [
                                        symbolName,
                                        symbolValue,
                                    ] = createdSymbol;
                                    const actual = mockCtx.get(symbolName);
                                    if (Array.isArray(symbolValue)) {
                                        strict.deepStrictEqual(
                                            actual,
                                            symbolValue,
                                        );
                                    } else {
                                        strict.strictEqual(actual, symbolValue);
                                    }
                                }
                            });
                        }
                    }
                });
            }
        });
    }
});
