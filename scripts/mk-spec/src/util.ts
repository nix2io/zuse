import { lstatSync, readdirSync, readFileSync } from "fs";
import { join } from "path";
import { parse } from "yaml";
import { LANG_DIR } from "./constants";

export const readYAMLFile = <T>(fileName: string): T =>
    parse(readFileSync(fileName, "utf-8"));

export const getGroupFunctions = (groupName: string): string[] => {
    const groupFolder = join(LANG_DIR, `${groupName}/`);
    const functions: string[] = [];
    readdirSync(groupFolder).forEach((file: string) => {
        if (lstatSync(join(groupFolder, file)).isFile()) {
            functions.push(file);
        }
    });
    return functions;
};

export const parseFunctionName = (name: string): string =>
    name
        .split(".zs")[0]
        .split("_")
        .map((n) => n[0].toUpperCase() + n.substr(1).toLowerCase())
        .join("");
