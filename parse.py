from utils import *
from tree import *

# 输入运算符到内部后缀运算符的映射 / Map input operators to internal postfix symbols
OP_MAP = {'+': '&', '|': '|', '^': '^'}
# 运算符优先级：数字越大优先级越高 / Operator precedence (higher value = higher priority)
PRECEDENCE = {'+': 3, '|': 2, '^': 1}


# 将表达式拆分成 token 列表 / Split an expression into a list of tokens
def tokenize(expr):
    tokens = []
    for c in expr.replace(' ', ''):
        if c in LETTERS:
            tokens.append(c)
        elif c in '+-|^!()':
            tokens.append(c)
        else:
            raise Exception(f"Invalid character '{c}' in expression")
    return tokens


# 用 Shunting-yard 算法把中缀表达式转成后缀式 / Convert infix expression to postfix using Shunting-yard
def infix_to_postfix(expr):
    tokens = tokenize(expr)
    if len(tokens) == 1 and tokens[0] in LETTERS:
        return tokens[0]

    output = []
    ops = []

    def flush_unary():
        # 遇到操作数后，把栈顶的单目运算符 ! 弹出到输出
        while ops and ops[-1] == '!':
            output.append(ops.pop())

    def pop_binary(token):
        # 遇到二元运算符时，弹出栈中优先级更高或相等的运算符
        while ops and ops[-1] != '(':
            top = ops[-1]
            if top == '!':
                break
            if PRECEDENCE[top] >= PRECEDENCE[token]:
                output.append(OP_MAP[ops.pop()])
            else:
                break

    for token in tokens:
        if token in LETTERS:
            # 字母：直接输出
            output.append(token)
            flush_unary()
        elif token == '!':
            # 非：压入运算符栈
            ops.append('!')
        elif token == '(':
            # 左括号：压栈，等待右括号匹配
            ops.append('(')
        elif token == ')':
            # 右括号：弹出运算符直到遇到左括号
            while ops and ops[-1] != '(':
                top = ops.pop()
                output.append('!' if top == '!' else OP_MAP[top])
            if not ops:
                raise Exception("Mismatched parentheses")
            ops.pop()
            flush_unary()
        elif token in OP_MAP:
            # 二元运算符：先弹出高优先级运算符，再压栈
            pop_binary(token)
            ops.append(token)
        else:
            raise Exception(f"Invalid token '{token}'")

    # 扫描结束后，清空运算符栈中剩余内容
    while ops:
        top = ops.pop()
        if top == '(':
            # 只有开括号、没有关括号
            raise Exception("Mismatched parentheses")
        output.append('!' if top == '!' else OP_MAP[top])

    return ''.join(output)


# 根据规则、查询和初始事实建立变量表 / Build variable map from rules, queries, and initial facts
def create_variables(rules, queries, facts):
    variables = {
        c: {"fact": Fact.FALSE, "verified": False}
        for r in rules
        for c in r["l_string"] + r["r_string"]
        if c in LETTERS
    }

    for c in queries:
        variables[c] = {"fact": Fact.FALSE, "verified": False}

    for c in facts:
        variables[c] = {"fact": Fact.TRUE, "verified": True}

    return variables


# 把原始规则转成后缀式并初始化变量 / Convert raw rules to postfix and initialize variables
def parse(raw_rules, facts, queries):
    rules = [{
        "l_string": infix_to_postfix(lhs),
        "r_string": infix_to_postfix(rhs),
        "l_tree": create_tree(infix_to_postfix(lhs)),
        "r_tree": create_tree(infix_to_postfix(rhs))
    } for lhs, rhs in raw_rules]

    variables = create_variables(rules, queries, facts)

    return rules, variables, queries
