#Coder : Muhammad Hamza
#Github: https://github.com/Hamzahash
#Facebook:Muhammad Hamza
#Youtube: HOP Anonymous
#Whatsapp:+92309-7992202
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))