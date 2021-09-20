class ANode {
    token_type
    token_value

    constructor(type, value) {
        this.token_type = type
        this.token_value = value
    }
}

const OPERATION = 'операция'
const PARENTHESES = 'скобка'
const DIGIT = 'число'
const operationReg = /[+\-*/]/g
const parenthesesReg = /[()]/g
const digitReg = /[0-9]+/g

function parseString(input) {
    const result = []
    for (let char of input) {
        if (operationReg.test(char)) {
            result.push(new ANode(OPERATION, char))
        } else if (parenthesesReg.test(char)) {
            result.push(new ANode(PARENTHESES, char))
        } else {
            result.push(new ANode(DIGIT, char))
        }
    }
    return result
}
