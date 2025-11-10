import sys

#  nó da árvore
class Node():
    def __init__(self, key, value):
        self.key = key      # Chave 
        self.value = value  # Valor 
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1      # 1 = Vermelho, 0 = Preto

# Classe principal da Árvore Red-Black
class RedBlackTree():
    def __init__(self):
        # Nó sentinela (NIL)
        self.TNULL = Node(0, None)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.count = 0 # Contador de nós

    # Rotação à esquerda no nó x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Rotação à direita no nó x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Inserção
    def insert(self, key, value):
        # Cria o novo nó
        node = Node(key, value)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1  # Novo nó é sempre vermelho
        self.count += 1

        y = None
        x = self.root

        # Encontra a posição correta para inserir
        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        # y é o pai do novo nó
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # Se o novo nó é a raiz = preto
        if node.parent == None:
            node.color = 0
            return

        # Se o avô é nulo, não há nada a fazer
        if node.parent.parent == None:
            return

        # Corrige a árvore após a inserção
        self.insert_fixup(node)

    # Corrige a árvore após a inserção
    def insert_fixup(self, k):
        while k.parent.color == 1:  # Enquanto o pai for vermelho
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Tio
                if u.color == 1:
                    # Caso 1: Tio é vermelho
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Caso 2: Tio é preto, k é filho à esquerda
                        k = k.parent
                        self.right_rotate(k)
                    # Caso 3: Tio é preto, k é filho à direita
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # Tio

                if u.color == 1:
                    # Caso 1 (espelhado): Tio é vermelho
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # Caso 2 (espelhado): Tio é preto, k é filho à direita
                        k = k.parent
                        self.left_rotate(k)
                    # Caso 3 (espelhado): Tio é preto, k é filho à esquerda
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0
        
    # Exclusão

    # Encontra o nó com a chave fornecida
    def get_node(self, key):
        node = self.root
        while node != self.TNULL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    # Transplante (substitui subárvore u por subárvore v)
    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Exclui um nó
    def delete_node(self, key):
        z = self.get_node(key)
        if z == self.TNULL:
            print("Não foi possível encontrar a chave na árvore")
            return
        
        self.count -= 1
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fixup(x)

    # Corrige a árvore após a exclusão
    def delete_fixup(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    # Caso 1: Irmão é vermelho
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    # Caso 2: Irmão é preto, ambos os filhos do irmão são pretos
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        # Caso 3: Irmão é preto, filho esquerdo do irmão é vermelho, direito é preto
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    # Caso 4: Irmão é preto, filho direito do irmão é vermelho
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    # Caso 1 (espelhado)
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    # Caso 2 (espelhado)
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        # Caso 3 (espelhado)
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    # Caso 4 (espelhado)
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0
        
    # Fila de Prioridade
    
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def find_max_node(self):
        """ Retorna o nó com a maior chave (maior prioridade) """
        if self.root == self.TNULL:
            return self.TNULL
        return self.maximum(self.root)

    def get_all_tasks_in_order(self):
        """ Retorna uma lista de todas as tarefas, em ordem crescente de prioridade """
        results = []
        self._in_order_traversal(self.root, results)
        return results

    def _in_order_traversal(self, node, results_list):
        if node != self.TNULL:
            self._in_order_traversal(node.left, results_list)
            
            task_list_formatted = [{'id': t['id'], 'name': t['name']} for t in node.value]
            results_list.append({
                'priority': node.key,
                'tasks': task_list_formatted
            })
            
            self._in_order_traversal(node.right, results_list)