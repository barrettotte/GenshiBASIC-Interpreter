PUNCTUATION = [
    "(",
    ")",
    ";",
    ":",
    ",",
    ".",
    "\""
]
OPERATORS = [
    "+",
    "-",
    "/",
    "*",
    "^",
    "=",
    "<",
    ">",
    "<>",
    "<=",
    "=<",
    ">=",
    "=>"
]
COMMANDS = [
    { "cmd": "ABS",    "type": "ONE-PARAM" },
    { "cmd": "AND",    "type": "BOOLEAN" },
    { "cmd": "ASC",    "type": "ONE-PARAM" },
    { "cmd": "ATN",    "type": "ONE-PARAM" },
    { "cmd": "CHR$",   "type": "ONE-PARAM" },
    { "cmd": "COS",    "type": "ONE-PARAM" },
    { "cmd": "DEF",    "type": "FUNCTION" },
    { "cmd": "DIM",    "type": "VAR-DEF" },
    { "cmd": "END",    "type": "NO-PARAM" },
    { "cmd": "EXP",    "type": "ONE-PARAM" },
    { "cmd": "FN",     "type": "FUNCTION" },
    { "cmd": "FOR",    "type": "FOR-DEF" },
    { "cmd": "GOSUB",  "type": "FLOW-CONTROL" },
    { "cmd": "GOTO",   "type": "FLOW-CONTROL" },
    { "cmd": "IF",     "type": "IF-DEF" },
    { "cmd": "INT",    "type": "ONE-PARAM" },
    { "cmd": "LEFT$",  "type": "TWO-PARAM" },
    { "cmd": "LEN",    "type": "ONE-PARAM" },
    { "cmd": "LET",    "type": "VAR-DEF" },
    { "cmd": "LOG",    "type": "ONE-PARAM" },
    { "cmd": "MID$",   "type": "THREE-PARAM" },
    { "cmd": "NEXT",   "type": "FOR-DEF" },
    { "cmd": "NOT",    "type": "BOOLEAN" },
    { "cmd": "OR",     "type": "BOOLEAN" },
    { "cmd": "PRINT",  "type": "PRINT" },
    { "cmd": "REM",    "type": "COMMENT" },
    { "cmd": "RETURN", "type": "NO-PARAM" },
    { "cmd": "RIGHT$", "type": "TWO-PARAM" },
    { "cmd": "RND",    "type": "ONE-PARAM" },
    { "cmd": "SGN",    "type": "ONE-PARAM" },
    { "cmd": "SIN",    "type": "ONE-PARAM" },
    { "cmd": "SPC",    "type": "ONE-PARAM" },
    { "cmd": "SQR",    "type": "ONE-PARAM" },
    { "cmd": "STEP",   "type": "FOR-DEF" },
    { "cmd": "STR$",   "type": "ONE-PARAM" },
    { "cmd": "TAB",    "type": "ONE-PARAM" },
    { "cmd": "TAN",    "type": "ONE-PARAM" },
    { "cmd": "THEN",   "type": "IF-DEF" },
    { "cmd": "TO",     "type": "FOR-DEF" }
]