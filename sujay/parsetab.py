
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DO ELSE EQ GE GT IDENTIFIER IF LBRACE LE LPAREN LT NE NUMBER PLUS RBRACE RPAREN SEMI WHILEprogram : statementsif_statement : IF LPAREN condition RPAREN block else_blockelse_block : ELSE block\n                  | emptywhile_statement : WHILE LPAREN condition RPAREN blockdo_while_statement : DO block WHILE LPAREN condition RPAREN SEMIcondition : expression EQ expression\n                 | expression NE expression\n                 | expression LT expression\n                 | expression GT expression\n                 | expression LE expression\n                 | expression GE expressionblock : LBRACE statements RBRACEstatements : statement statements\n                  | statement\n                  | if_statement statements\n                  | if_statement\n                  | while_statement statements\n                  | while_statement\n                  | do_while_statement statements\n                  | do_while_statementstatement : expression SEMI\n                 | IDENTIFIER ASSIGN expression SEMIexpression : IDENTIFIER\n                  | NUMBER\n                  | expression PLUS expressionempty :'
    
_lr_action_items = {'IDENTIFIER':([0,3,4,5,6,17,18,19,20,21,23,32,34,35,36,37,38,39,41,42,43,50,52,54,56,57,],[8,8,8,8,8,-22,25,25,25,25,8,-23,25,25,25,25,25,25,25,-13,-27,-5,-2,-4,-3,-6,]),'IF':([0,3,4,5,6,17,23,32,42,43,50,52,54,56,57,],[9,9,9,9,9,-22,9,-23,-13,-27,-5,-2,-4,-3,-6,]),'WHILE':([0,3,4,5,6,17,22,23,32,42,43,50,52,54,56,57,],[10,10,10,10,10,-22,30,10,-23,-13,-27,-5,-2,-4,-3,-6,]),'DO':([0,3,4,5,6,17,23,32,42,43,50,52,54,56,57,],[11,11,11,11,11,-22,11,-23,-13,-27,-5,-2,-4,-3,-6,]),'NUMBER':([0,3,4,5,6,17,18,19,20,21,23,32,34,35,36,37,38,39,41,42,43,50,52,54,56,57,],[12,12,12,12,12,-22,12,12,12,12,12,-23,12,12,12,12,12,12,12,-13,-27,-5,-2,-4,-3,-6,]),'$end':([1,2,3,4,5,6,13,14,15,16,17,32,42,43,50,52,54,56,57,],[0,-1,-15,-17,-19,-21,-14,-16,-18,-20,-22,-23,-13,-27,-5,-2,-4,-3,-6,]),'RBRACE':([3,4,5,6,13,14,15,16,17,31,32,42,43,50,52,54,56,57,],[-15,-17,-19,-21,-14,-16,-18,-20,-22,42,-23,-13,-27,-5,-2,-4,-3,-6,]),'SEMI':([7,8,12,24,25,26,55,],[17,-24,-25,-26,-24,32,57,]),'PLUS':([7,8,12,24,25,26,28,44,45,46,47,48,49,],[18,-24,-25,18,-24,18,18,18,18,18,18,18,18,]),'ASSIGN':([8,],[19,]),'LPAREN':([9,10,30,],[20,21,41,]),'LBRACE':([11,33,40,53,],[23,23,23,23,]),'EQ':([12,24,25,28,],[-25,-26,-24,34,]),'NE':([12,24,25,28,],[-25,-26,-24,35,]),'LT':([12,24,25,28,],[-25,-26,-24,36,]),'GT':([12,24,25,28,],[-25,-26,-24,37,]),'LE':([12,24,25,28,],[-25,-26,-24,38,]),'GE':([12,24,25,28,],[-25,-26,-24,39,]),'RPAREN':([12,24,25,27,29,44,45,46,47,48,49,51,],[-25,-26,-24,33,40,-7,-8,-9,-10,-11,-12,55,]),'ELSE':([42,43,],[-13,53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,3,4,5,6,23,],[2,13,14,15,16,31,]),'statement':([0,3,4,5,6,23,],[3,3,3,3,3,3,]),'if_statement':([0,3,4,5,6,23,],[4,4,4,4,4,4,]),'while_statement':([0,3,4,5,6,23,],[5,5,5,5,5,5,]),'do_while_statement':([0,3,4,5,6,23,],[6,6,6,6,6,6,]),'expression':([0,3,4,5,6,18,19,20,21,23,34,35,36,37,38,39,41,],[7,7,7,7,7,24,26,28,28,7,44,45,46,47,48,49,28,]),'block':([11,33,40,53,],[22,43,50,56,]),'condition':([20,21,41,],[27,29,51,]),'else_block':([43,],[52,]),'empty':([43,],[54,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','lexer.py',56),
  ('if_statement -> IF LPAREN condition RPAREN block else_block','if_statement',6,'p_if_statement','lexer.py',60),
  ('else_block -> ELSE block','else_block',2,'p_else_block','lexer.py',64),
  ('else_block -> empty','else_block',1,'p_else_block','lexer.py',65),
  ('while_statement -> WHILE LPAREN condition RPAREN block','while_statement',5,'p_while_statement','lexer.py',69),
  ('do_while_statement -> DO block WHILE LPAREN condition RPAREN SEMI','do_while_statement',7,'p_do_while_statement','lexer.py',73),
  ('condition -> expression EQ expression','condition',3,'p_condition','lexer.py',77),
  ('condition -> expression NE expression','condition',3,'p_condition','lexer.py',78),
  ('condition -> expression LT expression','condition',3,'p_condition','lexer.py',79),
  ('condition -> expression GT expression','condition',3,'p_condition','lexer.py',80),
  ('condition -> expression LE expression','condition',3,'p_condition','lexer.py',81),
  ('condition -> expression GE expression','condition',3,'p_condition','lexer.py',82),
  ('block -> LBRACE statements RBRACE','block',3,'p_block','lexer.py',86),
  ('statements -> statement statements','statements',2,'p_statements','lexer.py',90),
  ('statements -> statement','statements',1,'p_statements','lexer.py',91),
  ('statements -> if_statement statements','statements',2,'p_statements','lexer.py',92),
  ('statements -> if_statement','statements',1,'p_statements','lexer.py',93),
  ('statements -> while_statement statements','statements',2,'p_statements','lexer.py',94),
  ('statements -> while_statement','statements',1,'p_statements','lexer.py',95),
  ('statements -> do_while_statement statements','statements',2,'p_statements','lexer.py',96),
  ('statements -> do_while_statement','statements',1,'p_statements','lexer.py',97),
  ('statement -> expression SEMI','statement',2,'p_statement','lexer.py',104),
  ('statement -> IDENTIFIER ASSIGN expression SEMI','statement',4,'p_statement','lexer.py',105),
  ('expression -> IDENTIFIER','expression',1,'p_expression','lexer.py',112),
  ('expression -> NUMBER','expression',1,'p_expression','lexer.py',113),
  ('expression -> expression PLUS expression','expression',3,'p_expression','lexer.py',114),
  ('empty -> <empty>','empty',0,'p_empty','lexer.py',121),
]
