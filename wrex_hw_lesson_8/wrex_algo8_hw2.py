# -----------------------------------------------------------------------------
#                                   Задача
# 8.2 Закодируйте любую строку из трех слов по алгоритму Хаффмана.

#
# -----------------------------------------------------------------------------
#                                     Данные
import random as rand


words_1 = ['Аист', 'Берёза', 'Вася', 'Годзилла', 'Дочка',
           'Ёжик', 'Жена', 'Зёбра', 'Игнат', 'Кеша',
           'Ласка', 'Мама', 'Носорог', 'Петя', 'Тётя']
words_2 = ['атакует', 'баюкает', 'возит', 'гладит', 'готовит',
           'зовёт', 'игнорит', 'любит', 'моет', 'мучает',
           'кушает', 'пинает', 'ненавидит', 'приветствует', 'тащит']
words_3 = ['атлетику', 'бобров', 'девочек', 'годзиллу', 'дурачка',
           'ёжиков', 'жижу', 'занятия', 'забор', 'коров',
           'пинки', 'раму', 'носорога', 'чуждое', 'хлам']


def rnd(a: list, b: list, c: list):
    return ''.join([a[rand.randint(0, len(a)-1)], ' ', b[rand.randint(0, len(b)-1)], ' ', c[rand.randint(0, len(c)-1)]])


# -----------------------------------------------------------------------------
#                                    Древо
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def nodes(self):
        return self.left, self.right

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, left=True, binary_string=''):
    if type(node) is str:
        return {node: binary_string}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binary_string + '0'))
    d.update(huffman_code_tree(r, False, binary_string + '1'))
    return d


# -----------------------------------------------------------------------------
#                                    Генератор весов
def get_weights(st: str):
    wt = {}
    for s in st:
        if s in wt:
            wt[s] += 1
        else:
            wt[s] = 1
    wt = sorted(wt.items(), key=lambda x: x[1], reverse=True)
    return wt


def to_nodes(nodes: list):
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, (c1 + c2)))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes


# -----------------------------------------------------------------------------
#                                      main func
def main(st: str):
    print(f'{st=}')
    w_dict = get_weights(st)
    print(f'{w_dict=} ')
    nodes = to_nodes(w_dict)
    huffman_code = huffman_code_tree(nodes[0][0])
    for (char, frequency) in w_dict:
        print(' %-4r |%12s' % (char, huffman_code[char]))


# -----------------------------------------------------------------------------
#
main(rnd(words_1, words_2, words_3))
