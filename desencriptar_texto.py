def calcular_frecuencia(texto):
    frecuencia = {}
    letras_validas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÑ'
    
    for letra in texto:
        letra = letra.upper()  # Convertimos la letra a mayúscula para hacer la comparación
        if letra in letras_validas:
            if letra in frecuencia:
                frecuencia[letra] += 1
            else:
                frecuencia[letra] = 1
    return frecuencia

def descifrar_mensaje(cifrado):
    letras_validas = 'ABCDEFGHIJKLMNOPQRSTUVWXYÑZ'
    frecuencia_cifrado = calcular_frecuencia(cifrado)
    letras_espanol = 'EAROINLDCUTSMPBFVQJGHXZÑYKW'
    letras_ordenadas = sorted(frecuencia_cifrado, key=lambda letra: frecuencia_cifrado[letra], reverse=True)
    mapeo = {}
    for i in range(min(len(letras_espanol), len(letras_ordenadas))):  # Usamos el mínimo de ambas longitudes
        mapeo[letras_ordenadas[i]] = letras_espanol[i]
    mensaje_descifrado = ''
    for letra in cifrado:
        letra = letra.upper()  # Convertimos la letra a mayúscula para hacer la comparación
        if letra in letras_validas:
            mensaje_descifrado += mapeo[letra]
        else:
            mensaje_descifrado += letra
    return mensaje_descifrado

mensaje_cifrado = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJE, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."

mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)

print(mensaje_descifrado)
