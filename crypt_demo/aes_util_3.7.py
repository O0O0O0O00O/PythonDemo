#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/15 9:59
# @Author  : Nana Xing
# @File    : aes_util_3.7.py
# @ProjectName: tyautotest
# @Software : PyCharm
# @Description :AES CBC 128 加解密算法
"""
Python 3.7
AES CBC 128
AES 加解密
AES 加解密文件
ERROR：can't concat str to bytes
解决方法：https://stackoverflow.com/questions/40207259/typeerror-cant-concat-bytes-to-str-pycrypto-aes-encryption

ERROR : TypeError: ord() expected string of length 1, but int found
解决方法：https://stackoverflow.com/questions/43274703/trouble-with-encode-encrypt-pad-using-same-code-for-python2-and-python3
"""
import binascii

import os

from Crypto.Cipher import AES


class AESUtil:
    def __generate_iv(self):
        iv = b'884228eb5e53a57bd0511adb60fffa8d'
        return iv

    def __pad(self, text):
        """填充方式，加密内容必须为16字节的倍数，若不足则使用self.iv进行填充"""
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        # 适用python3 否则报错ERROR：can't concat str to bytes
        pad=bytes(pad,encoding="ascii")
        return text + pad * amount_to_pad

    def __unpad(self, text):
        #  ASCII 数值
        # pad = ord(text[-1])
        pad=ord(text[-1:])
        return text[:-pad]

    def aes_encrypt(self, plain_data, key, iv):
        """
        AES CBC 128
        CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)
        加密函数，如果data不是16的倍数【加密文本data必须为16的倍数！】，那就补足为16的倍数
        :param plain_data:明文数据 16位
        :param key:  16位
        :param iv:16位
        """
        cipher = AES.new(key, AES.MODE_CBC, iv)  # 设置AES加密模式 此处设置为CBC模式

        # 填充数据
        pad_data = self.__pad(text=plain_data)

        encrypted_data = cipher.encrypt(pad_data)  # aes加密
        # b2a_hex encode  将二进制转换成16进制,返回的二进制数据的十六进制表示。每一个字节的数据转换成相应的2位十六进制表示。
        # result = binascii.b2a_hex(encrypted_data)
        return encrypted_data

    def aes_decryppt(self, enc_data, key, iv):
        """
        AES 解密
        :param key:
        :param data:
        """
        cipher = AES.new(key, AES.MODE_CBC, iv)
        dec_data = cipher.decrypt(enc_data)

        unpad_data = self.__unpad(dec_data)
        # 字符串转16进制
        # result = binascii.hexlify(unpad_data)
        return unpad_data

    def enc_file(self, plain_file_path, enc_file_path, key):
        """
        加密文件
        :param plain_file_path: 明文文件路径
        :param enc_file_path: 加密后文件路径
        :param key: 秘钥
        :return:
        """
        # 16进制转字符串
        # key = binascii.a2b_hex(key)
        # iv = binascii.a2b_hex(self.__generate_iv())
        # 加密向量
        iv = key
        # iv = os.urandom(16)

        with open(plain_file_path, 'rb') as fileobj:
            content = fileobj.read()
            # 加密文件
            enc_content = self.aes_encrypt(plain_data=content, key=key, iv=iv)
        file_name = os.path.basename(plain_file_path)
        # out_file_path = os.path.dirname(plain_file_path) + '\\enc_obama.jpg'

        with open(enc_file_path, 'wb') as f:  # 以二进制写类型打开
            f.write(enc_content)  # 写入文件

    def dec_file(self, enc_file_path, dec_file_path, key):
        """
        解密文件
        :param enc_file_path: 加密文件路径
        :param dec_file_path: 解密文件路径
        :param key: 秘钥
        :return:
        """
        # 向量
        iv = key

        with open(enc_file_path, 'rb') as fileobj:
            content = fileobj.read()
            # 解密文件
            dec_content = self.aes_decryppt(enc_data=content, key=key, iv=iv)
        file_name = os.path.basename(enc_file_path)

        # (filename, extension) = os.path.splitext(file_name)
        # dec_file_path = os.path.dirname(enc_file_path) + '\\dec_obama.jpg'
        with open(dec_file_path, 'wb') as f:  # 以二进制写类型打开
            f.write(dec_content)  # 写入文件

    def getFilePath(self, fileType):
        """
        根据文件类型，获取文件路径
        :param fileType:
        :return:
        """
        dictory = os.path.dirname(os.path.abspath(__file__)) + '\data'
        if fileType == "video":
            filePath = dictory + "\jupiter_8k_16bit_mono.raw"
        elif fileType == "picture":
            filePath = dictory + "\obama.jpg"
        else:
            filePath = dictory + "\jupiter_8k_16bit_mono.raw"
        return filePath


if __name__ == '__main__':
    aes_util = AESUtil()
    encryptKey = '1234567887654321'

    plain_file_path = aes_util.getFilePath("picture")

    enc_file_path = os.path.dirname(plain_file_path) + '\\enc_obama.jpg'
    dec_file_path=os.path.dirname(enc_file_path)+'\\dec_obama.jpg'

    # 加密图片
    aes_util.enc_file(plain_file_path=plain_file_path, enc_file_path=enc_file_path, key=encryptKey)

    # 解密图片
    aes_util.dec_file(enc_file_path=enc_file_path, dec_file_path=dec_file_path, key=encryptKey)
