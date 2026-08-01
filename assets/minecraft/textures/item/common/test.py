from PIL import Image

# 画像の読み込み（RGBAとして読み込む）
img = Image.open('light_pillar.png').convert('RGBA')

# アルファチャンネル（透明度）を分離
alpha = img.split()[3]

# RGB部分のみをグレースケールに変換
gray = img.convert('L').convert('RGB')

# グレースケール画像に元のアルファチャンネルを再結合
gray_img = Image.merge('RGBA', (gray.split()[0], gray.split()[1], gray.split()[2], alpha))

# 保存
gray_img.save('light_pillar_1.png')