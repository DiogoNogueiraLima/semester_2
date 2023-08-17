# semester_2

Second semester projects of the Information Systems course.

```python
  def saiu(self):
        actual_node = self.initial_node
        # caso só tenha uma pessoa da fila
        if actual_node.next is None:
            self.dinheiro += actual_node.value
            self.initial_node = None
            self.last_node = None
        # sai o primeiro da fila e arrecada o dinheiro pago
        else:
            self.dinheiro += actual_node.value
            self.initial_node = actual_node.next
            actual_node.next.last = None
        self.size -= 1
        print(f'{actual_node.name} foi chamado para o caixa {self.caixa}')
```

qulaereru
