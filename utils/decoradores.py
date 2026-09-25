import time




def marcar_tempo_de_execucao(funcao_com_retorno=False):
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