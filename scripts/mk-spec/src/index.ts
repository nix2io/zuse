import { parse } from "@nix2/zuse-stdsyntax";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "fs";
import { join } from "path";
import { exit } from "process";
import {
    GENERATED_SPEC_FILE_NAME,
    LANG_DIR,
    SPECIFICATION_FILE,
} from "./constants";
import { BaseSpecType, LanguageSpecificationType } from "./types";
import { getGroupFunctions, parseFunctionName, readYAMLFile } from "./util";

console.log("Building Spec");

const baseSpec = <BaseSpecType>readYAMLFile(SPECIFICATION_FILE);
let languageSpecification: LanguageSpecificationType = {
    version: baseSpec.version,
    groups: baseSpec.groups,
    stdlib: {},
    coreFunctions: baseSpec.coreFunctions,
};

for (const groupName of baseSpec.groups) {
    const functionNames = getGroupFunctions(groupName);

    for (const functionName of functionNames) {
        const functionSourceCode = readFileSync(
            join(LANG_DIR, groupName, functionName),
            "utf-8",
        );
        const [funcSpec, error] = parse(functionName, functionSourceCode);
        if (error) {
            console.log(error.toString());
            exit(1);
        }

        languageSpecification.stdlib[
            parseFunctionName(functionName)
        ] = funcSpec as any;
    }
}

if (!existsSync("./out/")) mkdirSync("./out/");

writeFileSync(
    join("./out/", GENERATED_SPEC_FILE_NAME),
    JSON.stringify(languageSpecification),
);

console.log("Spec Built");
