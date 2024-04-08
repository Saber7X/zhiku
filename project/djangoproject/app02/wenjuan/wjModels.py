from django.db import models


# Create your models here.

class Disc(models.Model):
    yi_choices = (  # 新建选择字段
        (1, '富于冒险:愿意面对新事物并敢于下决心掌握的人'),
        (3, '适应力强:轻松自如适应任何环境'),
        (2, '生动:充满活力,表情生动,多手势'),
        (4, '善于分析:喜欢研究各部分之间的逻辑和正确的关系'),
    )
    er_choices = (  # 新建选择字段
        (3, '坚持不懈：要完成现有的事才能做新的事情'),
        (2, '喜好娱乐：开心充满乐趣与幽默感'),
        (4, '善于说服：用逻辑和事实而不用威严和权利服人'),
        (1, '平和：在冲突中不受干扰，保持平静'),
    )
    san_choices = (  # 新建选择字段
        (4, '顺服：易接受他人的观点和喜好，不坚持己见'),
        (3, '自我牺牲：为他人利益愿意放弃个人意见'),
        (1, '善于社交：认为与人相处是好玩，而不是挑战或者商业机会'),
        (2, '意志坚定：决心以自己的方式做事'),
    )
    si_choices = (  # 新建选择字段
        (3, '使人认同：因人格魅力或性格使人认同'),
        (1, '体贴：关心别人的感受与需要'),
        (4, '竞争性：把一切当作竞赛，总是有强烈的赢的欲望'),
        (2, '自控性：控制自己的情感，极少流露'),
    )
    wu_choices = (  # 新建选择字段
        (3, '使人振作：给他人清新振奋的刺激'),
        (1, '尊重他人：对人诚实尊重'),
        (4, '善于应变：对任何情况都能作出有效的反应'),
        (2, '含蓄：自我约束情绪与热忱'),
    )
    liu_choices = (  # 新建选择字段
        (4, '生机勃勃：充满生命力与兴奋'),
        (1, '满足：容易接受任何情况与环境'),
        (2, '敏感：对周围的人事过分关心'),
        (3, '自立：独立性强，只依靠自己的能力、判断、与才智'),
    )
    qi_choices = (  # 新建选择字段
        (3, '计划者：先做详尽的计划，并严格要计划进行，不想改动'),
        (4, '耐性：不因延误而懊恼，冷静且能容忍'),
        (2, '积极：相信自己有转危为安的能力'),
        (1, '推动者：动用性格魅力或鼓励别人参与'),
    )
    ba_choices = (  # 新建选择字段
        (1, '肯定：自信，极少犹豫或者动摇'),
        (2, '无拘无束：不喜欢预先计划，或者被计划牵制'),
        (3, '羞涩：安静，不善于交谈'),
        (4, '有时间性：生活处事依靠时间表，不喜欢计划被人干扰'),
    )
    jiu_choices = (  # 新建选择字段
        (4, '迁就：改变自己以与他人协调，短时间内按他人要求行事'),
        (3, '井井有条：有系统有条理安排事情的人'),
        (1, '坦率：毫无保留，坦率发言'),
        (2, '乐观：令他人和自己相信任何事情都会好转'),
    )
    shi_choices = (  # 新建选择字段
        (1, '强迫性：发号施令，强迫他人听从'),
        (3, '忠诚：一贯可靠，忠心不移，有时毫无根据地奉献'),
        (4, '有趣：风趣，幽默，把任何事物都能变成精彩的故事'),
        (2, '友善：不主动交谈，不爱争论'),
    )
    shiyi_choices = (  # 新建选择字段
        (1, '勇敢：敢于冒险，无所畏惧'),
        (4, '体贴：待人得体，有耐心'),
        (2, '注意细节：观察入微，做事情有条不紊'),
        (3, '可爱：开心，与他人相处充满乐趣'),
    )
    shier_choices = (  # 新建选择字段
        (3, '令人开心：充满活力，并将快乐传于他人'),
        (1, '文化修养：对艺术学术特别爱好，如戏剧、交响乐'),
        (4, '自信：确信自己个人能力与成功'),
        (2, '贯彻始终：情绪平稳，做事情坚持不懈'),
    )
    shisan_choices = (  # 新建选择字段
        (2, '理想主义：以自己完美的标准来设想衡量新事物'),
        (4, '独立：自给自足，独立自信，不需要他人帮忙'),
        (3, '无攻击性：不说或者做可能引起别人不满和反对的事情'),
        (1, '富有激励：鼓励别人参与、加入，并把每件事情变得有趣'),
    )
    shisi_choices = (  # 新建选择字段
        (3, '感情外露：从不掩饰情感.喜好,交谈时常身不由己接触他人'),
        (1, '深沉：深刻并常常内省，对肤浅的交谈、消遣会厌恶'),
        (4, '果断：有很快做出判断与结论的能力'),
        (2, '幽默：语气平和而有冷静的幽默'),
    )
    shiwu_choices = (  # 新建选择字段
        (3, '调解者：经常居中调节不同的意见，以避免双方的冲突'),
        (4, '音乐性：爱好参与并有较深的鉴赏能力，因音乐的艺术性,而不是因为表演的乐趣'),
        (1, '发起人：高效率的推动者，是他人的领导者，闲不住'),
        (2, '喜交朋友：喜欢周旋聚会中，善交新朋友不把任何人当陌生人'),
    )
    shiliu_choices = (  # 新建选择字段
        (2, '考虑周到：善解人意，帮助别人，记住特别的日子'),
        (3, '执着：不达目的，誓不罢休'),
        (4, '多言：不断的说话、讲笑话以娱乐他人，觉得应该避免沉默而带来的的尴尬'),
        (1, '容忍：易接受别人的想法和看法，不需要反对或改变他人'),
    )
    shiqi_choices = (  # 新建选择字段
        (3, '聆听者：愿意听别人倾诉'),
        (4, '忠心对自己的理想、朋友、工作都绝对忠实，有时甚至不需要理由'),
        (1, '领导者：天生的领导，不相信别人的能力能比上自己'),
        (2, '活力充沛：充满活力，精力充沛'),
    )
    shiba_choices = (  # 新建选择字段
        (2, '知足：满足自己拥有的，很少羡慕别人'),
        (4, '首领：要求领导地位及别人跟随'),
        (1, '制图者：用图表数字来组织生活，解决问题'),
        (3, '惹人喜爱：人们注意的中心，令人喜欢'),
    )
    shijiu_choices = (  # 新建选择字段
        (3, '完美主义者：对自己、对别人都高标准、一切事物有秩序'),
        (4, '和气：易相处，易说话，易让人接近'),
        (2, '勤劳：不停的工作，完成任务，不愿意休息'),
        (1, '受欢迎：聚会时的灵魂人物，受欢迎的宾客'),
    )
    ershi_choices = (  # 新建选择字段
        (2, '跳跃性：充满活力和生气勃勃'),
        (1, '无畏：大胆前进，不怕冒险'),
        (4, '规范性：时时坚持自己的举止合乎认同的道德规范'),
        (3, '平衡：稳定，走中间路线'),
    )
    ershiyi_choices = (  # 新建选择字段
        (4, '乏味：死气沉沉，缺乏生气'),
        (3, '忸怩：躲避别人的注意力，在众人注意下不自然'),
        (1, '露骨：好表现，华而不实，声音大'),
        (2, '专横：喜命令支配，有时略显傲慢'),
    )
    ershier_choices = (  # 新建选择字段
        (2, '散漫：生活任性无秩序'),
        (1, '无同情心：不易理解别人的问题和麻烦'),
        (3, '缺乏热情：不易兴奋，经常感到好事难做'),
        (4, '不宽恕：不易宽恕和忘记别人对自己的伤害，易嫉妒'),
    )
    ershisan_choices = (  # 新建选择字段
        (3, '保留：不愿意参与，尤其是当事情复杂时'),
        (4, '怨恨：把实际或者自己想象的别人的冒犯经常放在心中'),
        (1, '逆反：抗拒、或者拒不接受别人的方法，固执己见'),
        (2, '唠叨：重复讲同一件事情或故事，忘记已经重复多次，总是不断找话题说话'),
    )
    ershisi_choices = (  # 新建选择字段
        (4, '挑剔：坚持琐事细节，总喜欢挑不足'),
        (3, '胆小：经常感到强烈的担心焦虑、悲戚'),
        (2, '健忘：缺乏自我约束，导致健忘，不愿意回忆无趣的事情'),
        (1, '率直：直言不讳，直接表达自己的看法'),
    )
    ershiwu_choices = (  # 新建选择字段
        (1, '没耐性：难以忍受等待别人'),
        (4, '无安全感：感到担心且无自信心'),
        (2, '优柔寡断：很难下决定'),
        (3, '好插嘴：一个滔滔不绝的发言人，不是好听众，不注意别人的说话'),
    )
    ershiliu_choices = (  # 新建选择字段
        (4, '不受欢迎：由于强烈要求完美，而拒人千里'),
        (3, '不参与：不愿意加入，不参与，对别人生活不感兴趣'),
        (2, '难预测：时而兴奋，时而低落，或总是不兑现诺言'),
        (1, '缺同情心：很难当众表达对弱者或者受难者的情感'),
    )
    ershiqi_choices = (  # 新建选择字段
        (1, '固执：坚持照自己的意见行事，不听不同意见'),
        (2, '随兴：做事情没有一贯性，随意做事情'),
        (4, '难于取悦：因为要求太高而使别人很难取悦'),
        (3, '行动迟缓：迟迟才行动，不易参与或者行动总是慢半拍'),
    )
    ershiba_choices = (  # 新建选择字段
        (3, '平淡：平实淡漠，中间路线,无高低之分，很少表露情感'),
        (4, '悲观：尽管期待最好但往往首先看到事物不利之处'),
        (1, '自负：自我评价高，认为自己是最好的人选'),
        (2, '放任:许别人做他喜欢做的事情，为的是讨好别人，令别人鼓吹自己'),
    )
    ershijiu_choices = (  # 新建选择字段
        (3, '易怒：善变，孩子性格，易激动，过后马上就忘了'),
        (1, '无目标：不喜欢目标，也无意订目标'),
        (2, '好争论：易与人争吵，不管对何事都觉得自己是对的'),
        (4, '孤芳自赏：容易感到被疏离，经常没有安全感或担心别人不喜欢和自己相处'),
    )
    sanshi_choices = (  # 新建选择字段
        (3, '天真：孩子般的单纯，不理解生命的真谛'),
        (1, '消极：往往看到事物的消极面阴暗面，而少有积极的态度'),
        (4, '鲁莽：充满自信有胆识但总是不恰当'),
        (2, '冷漠：漠不关心，得过且过'),
    )
    sanshiyi_choices = (  # 新建选择字段
        (3, '担忧：时时感到不确定、焦虑、心烦'),
        (4, '不善交际:总喜欢挑人毛病，不被人喜欢'),
        (1, '工作狂:为了回报或者说成就感，而不是为了完美，因而设立雄伟目标不断工作，耻于休息'),
        (2, '喜获认同：需要旁人认同赞赏，像演员'),
    )
    sanshier_choices = (  # 新建选择字段
        (2, '过分敏感：对事物过分反应，被人误解时感到被冒犯'),
        (4, '不圆滑老练：经常用冒犯或考虑不周的方式表达自己'),
        (3, '胆怯：遇到困难退缩'),
        (2, '喋喋不休：难以自控，滔滔不绝，不能倾听别人'),
    )
    sanshisan_choices = (  # 新建选择字段
        (3, '腼腆：事事不确定，对所做的事情缺乏信心'),
        (2, '生活紊乱：缺乏安排生活的能力'),
        (1, '跋扈：冲动的控制事物和别人，指挥他人'),
        (4, '抑郁：常常情绪低落'),
    )
    sanshisi_choices = (  # 新建选择字段
        (3, '缺乏毅力：反复无常，互相矛盾，情绪与行动不合逻辑'),
        (1, '内向：活在自己的世界里，思想和兴趣放在心里'),
        (4, '不容忍：不能忍受他人的观点、态度和做事的方式'),
        (2, '无异议：对很多事情漠不关心'),
    )
    sanshiwu_choices = (  # 新建选择字段
        (4, '杂乱无章：生活环境无秩序，经常找不到东西'),
        (1, '情绪化：情绪不易高涨，感到不被欣赏时很容易低落'),
        (3, '喃喃自语：低声说话，不在乎说不清楚'),
        (2, '喜操纵：精明处事，操纵事情，使对自己有利'),
    )
    sanshiliu_choices = (  # 新建选择字段
        (2, '缓慢：行动思想均比较慢，过分麻烦'),
        (3, '顽固：决心依自己的意愿行事，不易被说服'),
        (1, '好表现：要吸引人，需要自己成为被人注意的中心'),
        (4, '有戒心：不易相信，对语言背后的真正的动机存在疑问'),
    )
    sanshiqi_choices = (  # 新建选择字段
        (2, '孤僻：需要大量的时间独处，避开人群'),
        (4, '统治欲：毫不犹豫地表示自己的正确或控制能力'),
        (3, '懒惰：总是先估量事情要耗费多少精力，能不做最好'),
        (1, '大嗓门：说话声和笑声总盖过他人'),
    )
    sanshiba_choices = (  # 新建选择字段
        (3, '拖延：凡事起步慢，需要推动力'),
        (4, '多疑：凡事怀疑，不相信别人'),
        (1, '易怒：对行动不快或不能完成指定工作时易烦躁和发怒'),
        (2, '不专注：无法专心致志或者集中精力'),
    )
    sanshijiu_choices = (  # 新建选择字段
        (4, '报复性：记恨并惩罚冒犯自己的人'),
        (2, '烦躁：喜新厌旧，不喜欢长时间做相同的事情'),
        (3, '勉强：不愿意参与或者说投入'),
        (1, '轻率：因没有耐心，不经思考，草率行动'),
    )
    sishi_choices = (  # 新建选择字段
        (3, '妥协：为避免矛盾即使自己是对的也不惜放弃自己的立场'),
        (4, '好批评：不断地衡量和下判断，经常考虑提出反对意见'),
        (1, '狡猾：精明，总是有办法达到目的'),
        (2, '善变：像孩子般注意力短暂，需要各种变化，怕无聊'),
    )
    username = models.CharField(null=True, blank=True, max_length=200)
    op0 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op1 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op2 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op3 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op4 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op5 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op6 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op7 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op8 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op9 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op10 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op11 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op12 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op13 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op14 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op15 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op16 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op17 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op18 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op19 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op20 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op21 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op22 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op23 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op24 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op25 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op26 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op27 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op28 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op29 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op30 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op31 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op32 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op33 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op34 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op35 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op36 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op37 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op38 = models.SmallIntegerField(null=True, blank=True, max_length=200)
    op39 = models.SmallIntegerField(null=True, blank=True, max_length=200)
