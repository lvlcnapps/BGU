import json

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)


    def nodes(self):
        return (self.left, self.right)


    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


def freq_start(input):
    with open(input, "r") as f, open("data.bin", "wb") as out, open("meta.json", "w") as m:
        data = f.read()
        # def comp(x):
        #     return len(x) > 0
        # data = filter(comp, data)
        freq = {}
        for c in data:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        nodes = freq

        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))

            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

        huffmanCode = huffman_code_tree(nodes[0][0])

        meta = {}
        for key, val in freq:
            meta[key] = huffmanCode[key]
        json.dump(meta, m)
        new_text = ''
        for c in data:
            new_text += huffmanCode[c]

        out.write(int(new_text, 2).to_bytes((len(new_text) + 7) // 8, byteorder='big'))

        # out.write(int(new_text, 2).to_bytes())
        print(' Char | Huffman code ')
        print('----------------------')
        for (char, frequency) in freq:
            print(' %-4r |%12s' % (char, huffmanCode[char]))
