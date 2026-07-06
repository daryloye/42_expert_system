import sys

VALID_EXPR_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ+-|^!() ')


# 读取并解析输入文件 / Read and parse the input file
def read(filepath=None):
    if filepath is None:
        if len(sys.argv) < 2:
            raise Exception("Usage: python main.py <input_file>")
        filepath = sys.argv[1]

    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise Exception(f"File not found: {filepath}")

    raw_rules = []
    facts = None
    queries = None

    for line_num, line in enumerate(lines, 1):
        line = line.split('#')[0].strip()
        if not line:
            continue

        if line.startswith('='):
            if facts is not None:
                raise Exception(f"Line {line_num}: duplicate facts declaration")
            facts_str = line[1:]
            for c in facts_str:
                if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    raise Exception(f"Line {line_num}: invalid fact '{c}'")
            facts = list(facts_str)

        elif line.startswith('?'):
            if queries is not None:
                raise Exception(f"Line {line_num}: duplicate queries declaration")
            queries_str = line[1:]
            for c in queries_str:
                if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    raise Exception(f"Line {line_num}: invalid query '{c}'")
            queries = list(queries_str)

        elif '<=>' in line:
            # 双向规则拆成两条单向规则
            lhs, rhs = line.split('<=>', 1)
            lhs, rhs = lhs.strip(), rhs.strip()
            validate_expression(lhs, line_num)
            validate_expression(rhs, line_num)
            raw_rules.append((lhs, rhs))
            raw_rules.append((rhs, lhs))

        elif '=>' in line:
            lhs, rhs = line.split('=>', 1)
            lhs, rhs = lhs.strip(), rhs.strip()
            validate_expression(lhs, line_num)
            validate_expression(rhs, line_num)
            raw_rules.append((lhs, rhs))

        else:
            raise Exception(f"Line {line_num}: invalid line format")

    if facts is None:
        facts = []
    if queries is None:
        raise Exception("Missing queries declaration")

    return raw_rules, facts, queries


# 校验表达式是否合法 / Validate that an expression contains only allowed characters
def validate_expression(expr, line_num):
    if not expr:
        raise Exception(f"Line {line_num}: empty expression")
    for c in expr:
        if c not in VALID_EXPR_CHARS:
            raise Exception(f"Line {line_num}: invalid character '{c}' in expression")
