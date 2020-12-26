export type GroupType = string;

export interface BaseSpecType {
    version: number;
    groups: GroupType;
    coreFunctions: string[];
}

export interface LanguageSpecificationType {
    version: number;
    groups: GroupType;
    stdlib: Record<string, [string, Record<string, unknown>]>;
    coreFunctions: string[];
}
