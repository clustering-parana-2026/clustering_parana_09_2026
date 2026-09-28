"""Decoradores para auxilir no projeto.

Implementa decorador para medir e exibir o tempo de execução de funções.
"""

import time




def marcar_tempo_de_execucao(funcao_com_retorno=False):
    """Crie um decorador que meça e exiba o tempo de execução.

    Parameters
    ----------
    funcao_com_retorno : bool, optional
        Se True, preserva o valor retornado pela função decorada.
        Se False, descarta esse valor e retorna None. O padrão é False.

    Returns
    -------
    callable
        Decorador que envolve uma função para medir seu tempo de
        execução e exibir seu nome e a duração em segundos.

    Notes
    -----
    A medição utiliza ``time.perf_counter`` e inclui apenas a chamada
    à função decorada, sem incluir a impressão do resultado da medição.

    Não gerencia exceções.

    Examples
    --------
    Para preservar o resultado da função:

    >>> @marcar_tempo_de_execucao(funcao_com_retorno=True)
    ... def somar(a, b):
    ...     return a + b

    Para uma função cujo retorno não será utilizado:

    >>> @marcar_tempo_de_execucao()
    ... def executar():
    ...     ...
    """
    def envelope_funcao(funcao):
        def envelope_argumentos(*args, **kwargs):
            inicio = time.perf_counter()
            
            if funcao_com_retorno:
                resultado = funcao(*args, **kwargs)
            else:
                funcao(*args, **kwargs)

            fim = time.perf_counter()
            tempo_de_execucao = fim - inicio
            print(30*'-')
            print(f'{f'"{funcao.__name__}":':50}{tempo_de_execucao:.6g} segundos')
            print(30*'-')

            if funcao_com_retorno:
                return resultado
            else:
                return None
            
        return envelope_argumentos
    return envelope_funcao 