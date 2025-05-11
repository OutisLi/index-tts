import torch
import platform

from indextts.infer import IndexTTS

if __name__ == "__main__":
    prompt_wav = "tests/zero_shot_prompt.wav"

    # default settings
    use_fp16 = torch.cuda.is_available()
    use_cuda_kernel = torch.cuda.is_available() and platform.system() == "Linux"

    tts = IndexTTS(
        cfg_path="checkpoints/config.yaml",
        model_dir="checkpoints",
        is_fp16=use_fp16,
        use_cuda_kernel=use_cuda_kernel,
    )
    # 长文本推理测试
    text = "《盗梦空间》是由美国华纳兄弟影片公司出品的电影，由克里斯托弗·诺兰执导并编剧，莱昂纳多·迪卡普里奥、玛丽昂·歌迪亚、约瑟夫·高登-莱维特、艾利奥特·佩吉、汤姆·哈迪等联袂主演，2010年7月16日在美国上映，2010年9月1日在中国内地上映，2020年8月28日在中国内地重映。影片剧情游走于梦境与现实之间，被定义为“发生在意识结构内的当代动作科幻片”，讲述了由莱昂纳多·迪卡普里奥扮演的造梦师，带领特工团队进入他人梦境，从他人的潜意识中盗取机密，并重塑他人梦境的故事。".replace(
        "\n", ""
    )
    tts.infer(
        audio_prompt=prompt_wav,
        text=text,
        output_path=f"outputs/{text[:20]}.wav",
        verbose=False,
    )
    # 并行长文本推理测试
    text = "《盗梦空间》是由美国华纳兄弟影片公司出品的电影，由克里斯托弗·诺兰执导并编剧，莱昂纳多·迪卡普里奥、玛丽昂·歌迪亚、约瑟夫·高登-莱维特、艾利奥特·佩吉、汤姆·哈迪等联袂主演，2010年7月16日在美国上映，2010年9月1日在中国内地上映，2020年8月28日在中国内地重映。影片剧情游走于梦境与现实之间，被定义为“发生在意识结构内的当代动作科幻片”，讲述了由莱昂纳多·迪卡普里奥扮演的造梦师，带领特工团队进入他人梦境，从他人的潜意识中盗取机密，并重塑他人梦境的故事。".replace(
        "\n", ""
    )
    tts.infer_fast(
        audio_prompt=prompt_wav,
        text=text,
        output_path=f"outputs/fast_{text[:20]}.wav",
        verbose=False,
    )
    text = "“在今天的大众媒体和图书市场上，到处充斥着关于潜能提升、心理操控、色彩星座、催眠读心等伪装成心理学的主题，\n更有一些伪心理学家、所谓的心理治疗师打着心理学的旗号欺世盗名，从中渔利。\n在浩如烟海、良莠不齐的心理学信息面前，如何拨除迷雾，去伪存真，成为一个明智的心理学信息的消费者呢？\n这本书将教给你科学实用的批判性思维技能，将真正的心理学研究从伪心理学中区分出来，告诉你什么才是真正的心理学。\n\n本书第1版出版于1983年，30多年来一直被奉为心理学入门经典，在全球顶尖大学中享有盛誉，现在呈现在读者面前的是第11版。\n这本书并不同于一般的心理学导论类教材，很多内容是心理学课堂上不曾讲授的，也是许多心理学教师在教学中感到只可意会不可言传的。\n作者正是从此初衷出发，以幽默生动的语言，结合一些妙趣横生、贴近生活的实例，深入浅出地介绍了可证伪性、操作主义、实证主义、安慰剂效应\n\nExcerpt From这才是心理学：看穿伪科学的批判性思维 (第11版)\n基思·斯坦诺维奇This material may be protected by copyright."
    tts.infer_fast(
        audio_prompt=prompt_wav,
        text=text,
        output_path=f"outputs/fast_{text[:20]}.wav",
        verbose=False,
    )
    #     # 单音频推理测试
    #     text = "晕 XUAN4 是 一 种 GAN3 觉"
    #     tts.infer(
    #         audio_prompt=prompt_wav,
    #         text=text,
    #         output_path=f"outputs/{text[:20]}.wav",
    #         verbose=True,
    #     )
    #     text = "大家好，我现在正在bilibili 体验 ai 科技，说实话，来之前我绝对想不到！AI技术已经发展到这样匪夷所思的地步了！"
    #     tts.infer(
    #         audio_prompt=prompt_wav,
    #         text=text,
    #         output_path=f"outputs/{text[:20]}.wav",
    #         verbose=True,
    #     )
    #     text = "There is a vehicle arriving in dock number 7?"
    #     tts.infer(
    #         audio_prompt=prompt_wav,
    #         text=text,
    #         output_path=f"outputs/{text[:20]}.wav",
    #         verbose=True,
    #     )
    #     text = "“我爱你！”的英语是“I love you!”"
    #     tts.infer(
    #         audio_prompt=prompt_wav,
    #         text=text,
    #         output_path=f"outputs/{text[:20]}.wav",
    #         verbose=True,
    #     )
    #     text = "Joseph Gordon-Levitt is an American actor"
    #     tts.infer(
    #         audio_prompt=prompt_wav,
    #         text=text,
    #         output_path=f"outputs/{text[:20]}.wav",
    #         verbose=True,
    #     )
    #     text = "约瑟夫·高登-莱维特是美国演员"
    #     tts.infer(
    #         audio_prompt=prompt_wav,
    #         text=text,
    #         output_path=f"outputs/{text[:20]}.wav",
    #         verbose=True,
    #     )
    #     text = "蒂莫西·唐纳德·库克（英文名：Timothy Donald Cook），通称蒂姆·库克（Tim Cook），现任苹果公司首席执行官。"
    #     tts.infer(
    #         audio_prompt=prompt_wav,
    #         text=text,
    #         output_path="outputs/蒂莫西·唐纳德·库克.wav",
    #         verbose=True,
    #     )
    #     # 并行推理测试
    #     text = "亲爱的伙伴们，大家好！每一次的努力都是为了更好的未来，要善于从失败中汲取经验，让我们一起勇敢前行,迈向更加美好的明天！"
    #     tts.infer_fast(
    #         audio_prompt=prompt_wav,
    #         text=text,
    #         output_path=f"outputs/{text[:20]}.wav",
    #         verbose=True,
    #     )
    #     text = "The weather is really nice today, perfect for studying at home.Thank you!"
    #     tts.infer_fast(
    #         audio_prompt=prompt_wav,
    #         text=text,
    #         output_path=f"outputs/{text[:20]}.wav",
    #         verbose=True,
    #     )
    #     text = """叶远随口答应一声，一定帮忙云云。
    # 教授看叶远的样子也知道，这事情多半是黄了。
    # 谁得到这样的东西也不会轻易贡献出来，这是很大的一笔财富。
    # 叶远回来后，又自己做了几次试验，发现空间湖水对一些外伤也有很大的帮助。
    # 找来一只断了腿的兔子，喝下空间湖水，一天时间，兔子就完全好了。
    # 还想多做几次试验，可是身边没有试验的对象，就先放到一边，了解空间湖水可以饮用，而且对人有利，这些就足够了。
    # 感谢您的收听，下期再见！
    #     """.replace("\n", "")
    #     tts.infer_fast(
    #         audio_prompt=prompt_wav,
    #         text=text,
    #         output_path=f"outputs/{text[:20]}.wav",
    #         verbose=True,
    #     )
