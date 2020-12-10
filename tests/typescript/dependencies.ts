/**
 * Class to represent a execution context.
 * @class Context
 */
export class Context {
    public symbols: Record<string, any>;

    /**
     * Constructor for a context.
     * @param {Record<string, any>} std_funcs Standard library.
     */
    constructor(
        public std_funcs: Record<string, any>,
        public config = { logFunc: console.log },
    ) {
        this.symbols = {};
    }

    /**
     * Get a symbol.
     * @param   {string} name Symbol name.
     * @returns {any}         Value of the symbol.
     */
    get(name: string): any {
        if (typeof name != "string") throw Error("symbol name is not a string");
        const val = this.symbols[name] || this.std_funcs[name];
        if (val == undefined) throw Error(name + " does not exist");
        return val;
    }

    /**
     * Set a symbol.
     * @param   {string} name  Symbol name.
     * @param   {PrimativeTypes | NodeType} value Symbol value.
     * @returns {PrimativeTypes | NodeType}       Symbol value given.
     */
    set(
        name: string,
        value: PrimativeTypes | NodeType,
    ): PrimativeTypes | NodeType {
        this.symbols[name] = value;
        return value;
    }

    /**
     * Computes the value of a given node or value.
     * @param {Node | PrimativeTypes} node_or_value Node or value.
     * @returns {PrimativeTypes} Value of a node or value.
     */
    val(node_or_value: Node | PrimativeTypes): PrimativeTypes {
        return node_or_value instanceof Node
            ? node_or_value.run(this)
            : node_or_value;
    }

    /**
     * Log something to the log in te config.
     * @param {any} value Value to log.
     */
    log(value: any) {
        this.config.logFunc(value);
    }
}

export type PrimativeTypes =
    | string
    | number
    | boolean
    | null
    | PrimativeTypes[];

export type ArgValType = PrimativeTypes | NodeType;

export type NodeType<T = string, O = Record<string, any>> = [T, O];

/**
 * Represent a node.
 */
export class Node<T extends string = string> {
    /**
     * Node constructor.
     * @param {string} type Type of node.
     * @param {Record<string, any>} args Node arguments.
     */
    constructor(public type: T, public args: Record<string, any>) {}

    /**
     * Run the node.
     * @param {Context} context Execution context.
     * @returns {any} Result of the node.
     */
    run(context: Context): any {
        const node = context.get(this.type);

        const nodeType = node[0];

        if (nodeType != "Function")
            throw Error(nodeType + " was used as a function");

        const functionArguments = node[1];
        const func = functionArguments["logic"];

        // some arg validation
        let result: any;
        if (typeof func == "function") {
            result = func(context, ...Object.values(this.args));
        } else {
            result = func.run(context);
        }

        // return type validation

        return result;
    }
}
