# Exercício Black Jack
import random
from random import randint


class BlackJack:

    def __init__(self):
        self.cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'K', 'J', 'A'] * 4
        self.pontuacao = 0
        self.varsorteio = 0

    def sorteio(self):
        random.shuffle(self.cartas)
        self.carta_sort = random.choice(self.cartas)

        if self.carta_sort == 'A':
            print(f"A carta sorteada foi {self.carta_sort}")
            if self.pontuacao <= 9 and self.pontuacao > 0:
                self.pontuacao += 1
                return self.pontuacao
            else:
                self.pontuacao += 11
                return self.pontuacao

        if self.carta_sort == 'Q' or self.carta_sort == 'K' or self.carta_sort == 'J':
            print(f"A carta sorteada foi {self.carta_sort} e seu valor é de: 10")
            self.pontuacao += 10
            print(f"Sua pontuação é de: {self.pontuacao}")
            return self.pontuacao

        if self.carta_sort == 10:
            print(f"A carta sorteada foi {self.carta_sort}")
            self.pontuacao += 10
            return self.pontuacao

        print(f"A carta sorteada foi: {self.carta_sort}")
        self.pontuacao += self.carta_sort
        print(f"Sua pontuação é de: {self.pontuacao}")
        return self.pontuacao

    def chama_carta(self):
        prgt = input(f"Deseja comprar mais uma carta?")
        if prgt == 's':
            self.varsorteio = self.sorteio()
            self.pontuacao = self.varsorteio
            return self.pontuacao
        if prgt == 'n':
            print(f"Você decidiu parar, sua pontuação: {self.pontuacao}")
            exit()
    def verifica_ponto(self):
        while self.pontuacao < 21:
            self.chama_carta()
        if self.pontuacao > 21:
            print(f"Você Perdeu!! \n Sua pontuação {self.pontuacao}")

        if self.pontuacao == 21:
            print(f"Você Venceu!! \n Sua pontuação {self.pontuacao}")
b = BlackJack()
b.sorteio()
b.verifica_ponto()
