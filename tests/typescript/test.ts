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
import { safeLoad } from "js-yaml";

// Define some paths
const ROOT_DIR = join("../../");
const SPECIFICATION_FILE = join(ROOT_DIR, "spec.yaml");
const LANG_DIR = join(ROOT_DIR, "lang/");
const TEMP_FILE = "tmp_logic.ts";

const getLanguageSpecification = (): {
    version: number;
    groups: string[];
} => safeLoad(readFileSync(SPECIFICATION_FILE, "utf-8")) as any;

const getGroupFunctions = (groupName: string): string[] => {
    const groupFolder = join(LANG_DIR, `${groupName}/`);
    const functions: string[] = [];
    readdirSync(groupFolder).forEach((file: string) => {
        if (lstatSync(join(groupFolder, file)).isDirectory()) {
            functions.push(file);
        }
    });
    return functions;
};

console.log("Running Typescript Tests");

console.log("Building Temp file");

// Get the language specification
const languageSpecification = getLanguageSpecification();
// Create the temp file
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
// Write the temp file
writeFileSync(TEMP_FILE, tempFileContent);

// Import the new temp file's functions
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
                    const funcSpecFile = join(funcDir, "spec.yaml");
                    let funcSpec;
                    try {

                        funcSpec = safeLoad(
                            readFileSync(funcSpecFile, "utf-8"),
                            ) as any;
                    } catch (e) {
                        console.error('Could not parse ' + funcName);
                        throw e;
                    }

                    const logicFunc =
                        logicFunctions[`${funcName.toLowerCase()}_logic`];

                    // ignore the test if not defined
                    if (typeof logicFunc == "undefined") return;
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
