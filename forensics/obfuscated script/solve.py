# el texto del txt
encrypted_text = """m/%(.itik9,*('2y+/<:*}=z-\x16*y-z\x16:=xxx\x16>y;":\x16\x7fq{z~}4kC,*!&im/%(.Cm|pqq*\x7fpy-x+{}x{{+\x7f*zq-z~{{(pz*}piti ,>dnn\x06+#,*=i\x1a0:=,$g ,=g\x1a&*",=:g\x1d\n\x19\n% ,'=anxp{gx\x7fqgx{\x7fgx}qnex{z}`rmxqxqy(px-*-(}-~++\x7f-|x-zz/y}*\x7fqqyitim|pqq*\x7fpy-x+{}x{{+\x7f*zq-z~{{(pz*}pg\x0e,=\x1a=;,($a`r\x12+0=,\x12\x14\x14m|-}{x,~\x7f-q/|}x*+p-+\x7fpq+~y|\x7fp(q*}itiygg\x7f||\x7fz|5l2y4r>! %,aam itimxqxqy(px-*-(}-~++\x7f-|x-zz/y}*\x7fqqyg\x1b,(-am|-}{x,~\x7f-q/|}x*+p-+\x7fpq+~y|\x7fp(q*}eiyeim|-}{x,~\x7f-q/|}x*+p-+\x7fpq+~y|\x7fp(q*}g\x05,'.=!``id',iy`2rm-(=(itia ,>dnn\x06+#,*=id\x1d09, ($,i\x1a0:=,$g\x1d,1=g\x08\x1a\n\x00\x0c'*&- '.`g\x0e,=\x1a=; '.am|-}{x,~\x7f-q/|}x*+p-+\x7fpq+~y|\x7fp(q*}eyeim `rm{|+}yx|x*{+q}p+{(\x7fpy,/(+,y/z}~|xitia kk,nn1im-(=(i{woxi5i\x0fkk<=d\x1a=; nn'.i`rmyz+y,x(y{-\x7fp}{q{p/{,}y\x7f{qz{*q}p\x7fitim{|+}yx|x*{+q}p+{(\x7fpy,/(+,y/z}~|xibin\x19\x1abinibia9kk>nn-`g\x19(=!ibinwinrm{|+/~\x7f+q~p}*}(z++/~(px{-q|(,(*p|itia\x12=,1=g,'*&- '.\x14ss\x08\x1a\n`g\x0e,=\x1a0=,:amyz+y,x(y{-\x7fp}{q{p/{,}y\x7f{qz{*q}p\x7f`rmxqxqy(px-*-(}-~++\x7f-|x-zz/y}*\x7fqqyg\x1e; =,am{|+/~\x7f+q~p}*}(z++/~(px{-q|(,(*p|eyem{|+/~\x7f+q~p}*}(z++/~(px{-q|(,(*p|g\x05,'.=`rmxqxqy(px-*-(}-~++\x7f-|x-zz/y}*\x7fqqyg\x0f%<:!a`4rm|pqq*\x7fpy-x+{}x{{+\x7f*zq-z~{{(pz*}pg\n%&:,a`C"""

# Aplicar la misma clave XOR (73) que usa el script original
decrypted_chars = [chr(ord(char) ^ 73) for char in encrypted_text]
decrypted_text = "".join(decrypted_chars)

print(decrypted_text)
