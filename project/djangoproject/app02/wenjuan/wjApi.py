from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from app02.wenjuan.wjModels import Disc
from app01.cert.models import Qiyeuser


@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4', 'GET'])
def Discget(request):
    if request.method == 'GET':
        data = (
            (
                {"op": 1, "content": '富于冒险:愿意面对新事物并敢于下决心掌握的人'},
                {"op": 3, "content": '适应力强:轻松自如适应任何环境'},
                {"op": 2, "content": '生动:充满活力,表情生动,多手势'},
                {"op": 4, "content": '善于分析:喜欢研究各部分之间的逻辑和正确的关系'},
            ),
            (
                {"op": 3, "content": '坚持不懈：要完成现有的事才能做新的事情'},
                {"op": 2, "content": '喜好娱乐：开心充满乐趣与幽默感'},
                {"op": 4, "content": '善于说服：用逻辑和事实而不用威严和权利服人'},
                {"op": 1, "content": '平和：在冲突中不受干扰，保持平静'},
            ),
            (
                {"op": 4, "content": '顺服：易接受他人的观点和喜好，不坚持己见'},
                {"op": 3, "content": '自我牺牲：为他人利益愿意放弃个人意见'},
                {"op": 1, "content": '善于社交：认为与人相处是好玩，而不是挑战或者商业机会'},
                {"op": 2, "content": '意志坚定：决心以自己的方式做事'},
            ),
            (
                {"op": 3, "content": '使人认同：因人格魅力或性格使人认同'},
                {"op": 1, "content": '体贴：关心别人的感受与需要'},
                {"op": 4, "content": '竞争性：把一切当作竞赛，总是有强烈的赢的欲望'},
                {"op": 2, "content": '自控性：控制自己的情感，极少流露'},
            ),
            (
                {"op": 3, "content": '使人振作：给他人清新振奋的刺激'},
                {"op": 1, "content": '尊重他人：对人诚实尊重'},
                {"op": 4, "content": '善于应变：对任何情况都能作出有效的反应'},
                {"op": 2, "content": '含蓄：自我约束情绪与热忱'},
            ),
            (
                {"op": 4, "content": '生机勃勃：充满生命力与兴奋'},
                {"op": 1, "content": '满足：容易接受任何情况与环境'},
                {"op": 2, "content": '敏感：对周围的人事过分关心'},
                {"op": 3, "content": '自立：独立性强，只依靠自己的能力、判断、与才智'},
            ),
            (
                {"op": 3, "content": '计划者：先做详尽的计划，并严格要计划进行，不想改动'},
                {"op": 4, "content": '耐性：不因延误而懊恼，冷静且能容忍'},
                {"op": 2, "content": '积极：相信自己有转危为安的能力'},
                {"op": 1, "content": '推动者：动用性格魅力或鼓励别人参与'},
            ),
            (
                {"op": 1, "content": '肯定：自信，极少犹豫或者动摇'},
                {"op": 2, "content": '无拘无束：不喜欢预先计划，或者被计划牵制'},
                {"op": 3, "content": '羞涩：安静，不善于交谈'},
                {"op": 4, "content": '有时间性：生活处事依靠时间表，不喜欢计划被人干扰'},
            ),
            (
                {"op": 4, "content": '迁就：改变自己以与他人协调，短时间内按他人要求行事'},
                {"op": 3, "content": '井井有条：有系统有条理安排事情的人'},
                {"op": 1, "content": '坦率：毫无保留，坦率发言'},
                {"op": 2, "content": '乐观：令他人和自己相信任何事情都会好转'},
            ),
            (
                {"op": 1, "content": '强迫性：发号施令，强迫他人听从'},
                {"op": 3, "content": '忠诚：一贯可靠，忠心不移，有时毫无根据地奉献'},
                {"op": 4, "content": '有趣：风趣，幽默，把任何事物都能变成精彩的故事'},
                {"op": 2, "content": '友善：不主动交谈，不爱争论'},
            ),
            (
                {"op": 1, "content": '勇敢：敢于冒险，无所畏惧'},
                {"op": 4, "content": '体贴：待人得体，有耐心'},
                {"op": 2, "content": '注意细节：观察入微，做事情有条不紊'},
                {"op": 3, "content": '可爱：开心，与他人相处充满乐趣'},
            ),
            (
                {"op": 3, "content": '令人开心：充满活力，并将快乐传于他人'},
                {"op": 1, "content": '文化修养：对艺术学术特别爱好，如戏剧、交响乐'},
                {"op": 4, "content": '自信：确信自己个人能力与成功'},
                {"op": 2, "content": '贯彻始终：情绪平稳，做事情坚持不懈'},
            ),
            (
                {"op": 2, "content": '理想主义：以自己完美的标准来设想衡量新事物'},
                {"op": 4, "content": '独立：自给自足，独立自信，不需要他人帮忙'},
                {"op": 3, "content": '无攻击性：不说或者做可能引起别人不满和反对的事情'},
                {"op": 1, "content": '富有激励：鼓励别人参与、加入，并把每件事情变得有趣'},
            ),
            (
                {"op": 3, "content": '感情外露：从不掩饰情感.喜好,交谈时常身不由己接触他人'},
                {"op": 1, "content": '深沉：深刻并常常内省，对肤浅的交谈、消遣会厌恶'},
                {"op": 4, "content": '果断：有很快做出判断与结论的能力'},
                {"op": 2, "content": '幽默：语气平和而有冷静的幽默'},
            ),
            (
                {"op": 3, "content": '调解者：经常居中调节不同的意见，以避免双方的冲突'},
                {"op": 4, "content": '音乐性：爱好参与并有较深的鉴赏能力，因音乐的艺术性,而不是因为表演的乐趣'},
                {"op": 1, "content": '发起人：高效率的推动者，是他人的领导者，闲不住'},
                {"op": 2, "content": '喜交朋友：喜欢周旋聚会中，善交新朋友不把任何人当陌生人'},
            ),
            (
                {"op": 2, "content": '考虑周到：善解人意，帮助别人，记住特别的日子'},
                {"op": 3, "content": '执着：不达目的，誓不罢休'},
                {"op": 4, "content": '多言：不断的说话、讲笑话以娱乐他人，觉得应该避免沉默而带来的的尴尬'},
                {"op": 1, "content": '容忍：易接受别人的想法和看法，不需要反对或改变他人'},
            ),
            (
                {"op": 3, "content": '聆听者：愿意听别人倾诉'},
                {"op": 4, "content": '忠心对自己的理想、朋友、工作都绝对忠实，有时甚至不需要理由'},
                {"op": 1, "content": '领导者：天生的领导，不相信别人的能力能比上自己'},
                {"op": 2, "content": '活力充沛：充满活力，精力充沛'},
            ),
            (
                {"op": 2, "content": '知足：满足自己拥有的，很少羡慕别人'},
                {"op": 4, "content": '首领：要求领导地位及别人跟随'},
                {"op": 1, "content": '制图者：用图表数字来组织生活，解决问题'},
                {"op": 3, "content": '惹人喜爱：人们注意的中心，令人喜欢'},
            ),
            (
                {"op": 3, "content": '完美主义者：对自己、对别人都高标准、一切事物有秩序'},
                {"op": 4, "content": '和气：易相处，易说话，易让人接近'},
                {"op": 2, "content": '勤劳：不停的工作，完成任务，不愿意休息'},
                {"op": 1, "content": '受欢迎：聚会时的灵魂人物，受欢迎的宾客'},
            ),
            (
                {"op": 2, "content": '跳跃性：充满活力和生气勃勃'},
                {"op": 1, "content": '无畏：大胆前进，不怕冒险'},
                {"op": 4, "content": '规范性：时时坚持自己的举止合乎认同的道德规范'},
                {"op": 3, "content": '平衡：稳定，走中间路线'},
            ),
            (
                {"op": 4, "content": '乏味：死气沉沉，缺乏生气'},
                {"op": 3, "content": '忸怩：躲避别人的注意力，在众人注意下不自然'},
                {"op": 1, "content": '露骨：好表现，华而不实，声音大'},
                {"op": 2, "content": '专横：喜命令支配，有时略显傲慢'},
            ),
            (
                {"op": 2, "content": '散漫：生活任性无秩序'},
                {"op": 1, "content": '无同情心：不易理解别人的问题和麻烦'},
                {"op": 3, "content": '缺乏热情：不易兴奋，经常感到好事难做'},
                {"op": 4, "content": '不宽恕：不易宽恕和忘记别人对自己的伤害，易嫉妒'},
            ),
            (
                {"op": 3, "content": '保留：不愿意参与，尤其是当事情复杂时'},
                {"op": 4, "content": '怨恨：把实际或者自己想象的别人的冒犯经常放在心中'},
                {"op": 1, "content": '逆反：抗拒、或者拒不接受别人的方法，固执己见'},
                {"op": 2, "content": '唠叨：重复讲同一件事情或故事，忘记已经重复多次，总是不断找话题说话'},
            ),
            (
                {"op": 4, "content": '挑剔：坚持琐事细节，总喜欢挑不足'},
                {"op": 3, "content": '胆小：经常感到强烈的担心焦虑、悲戚'},
                {"op": 2, "content": '健忘：缺乏自我约束，导致健忘，不愿意回忆无趣的事情'},
                {"op": 1, "content": '率直：直言不讳，直接表达自己的看法'},
            ),
            (
                {"op": 1, "content": '没耐性：难以忍受等待别人'},
                {"op": 4, "content": '无安全感：感到担心且无自信心'},
                {"op": 2, "content": '优柔寡断：很难下决定'},
                {"op": 3, "content": '好插嘴：一个滔滔不绝的发言人，不是好听众，不注意别人的说话'},
            ),
            (
                {"op": 4, "content": '不受欢迎：由于强烈要求完美，而拒人千里'},
                {"op": 3, "content": '不参与：不愿意加入，不参与，对别人生活不感兴趣'},
                {"op": 2, "content": '难预测：时而兴奋，时而低落，或总是不兑现诺言'},
                {"op": 1, "content": '缺同情心：很难当众表达对弱者或者受难者的情感'},
            ),
            (
                {"op": 1, "content": '固执：坚持照自己的意见行事，不听不同意见'},
                {"op": 2, "content": '随兴：做事情没有一贯性，随意做事情'},
                {"op": 4, "content": '难于取悦：因为要求太高而使别人很难取悦'},
                {"op": 3, "content": '行动迟缓：迟迟才行动，不易参与或者行动总是慢半拍'},
            ),
            (
                {"op": 3, "content": '平淡：平实淡漠，中间路线,无高低之分，很少表露情感'},
                {"op": 4, "content": '悲观：尽管期待最好但往往首先看到事物不利之处'},
                {"op": 1, "content": '自负：自我评价高，认为自己是最好的人选'},
                {"op": 2, "content": '放任:许别人做他喜欢做的事情，为的是讨好别人，令别人鼓吹自己'},
            ),
            (
                {"op": 3, "content": '易怒：善变，孩子性格，易激动，过后马上就忘了'},
                {"op": 1, "content": '无目标：不喜欢目标，也无意订目标'},
                {"op": 2, "content": '好争论：易与人争吵，不管对何事都觉得自己是对的'},
                {"op": 4, "content": '孤芳自赏：容易感到被疏离，经常没有安全感或担心别人不喜欢和自己相处'},
            ),
            (
                {"op": 3, "content": '天真：孩子般的单纯，不理解生命的真谛'},
                {"op": 1, "content": '消极：往往看到事物的消极面阴暗面，而少有积极的态度'},
                {"op": 4, "content": '鲁莽：充满自信有胆识但总是不恰当'},
                {"op": 2, "content": '冷漠：漠不关心，得过且过'},
            ),
            (
                {"op": 3, "content": '担忧：时时感到不确定、焦虑、心烦'},
                {"op": 4, "content": '不善交际:总喜欢挑人毛病，不被人喜欢'},
                {"op": 1, "content": '工作狂:为了回报或者说成就感，而不是为了完美，因而设立雄伟目标不断工作，耻于休息'},
                {"op": 2, "content": '喜获认同：需要旁人认同赞赏，像演员'},
            ),
            (
                {"op": 2, "content": '过分敏感：对事物过分反应，被人误解时感到被冒犯'},
                {"op": 4, "content": '不圆滑老练：经常用冒犯或考虑不周的方式表达自己'},
                {"op": 3, "content": '胆怯：遇到困难退缩'},
                {"op": 1, "content": '喋喋不休：难以自控，滔滔不绝，不能倾听别人'},
            ),
            (
                {"op": 3, "content": '腼腆：事事不确定，对所做的事情缺乏信心'},
                {"op": 2, "content": '生活紊乱：缺乏安排生活的能力'},
                {"op": 1, "content": '跋扈：冲动的控制事物和别人，指挥他人'},
                {"op": 4, "content": '抑郁：常常情绪低落'},
            ),
            (
                {"op": 3, "content": '缺乏毅力：反复无常，互相矛盾，情绪与行动不合逻辑'},
                {"op": 1, "content": '内向：活在自己的世界里，思想和兴趣放在心里'},
                {"op": 4, "content": '不容忍：不能忍受他人的观点、态度和做事的方式'},
                {"op": 2, "content": '无异议：对很多事情漠不关心'},
            ),
            (
                {"op": 4, "content": '杂乱无章：生活环境无秩序，经常找不到东西'},
                {"op": 1, "content": '情绪化：情绪不易高涨，感到不被欣赏时很容易低落'},
                {"op": 3, "content": '喃喃自语：低声说话，不在乎说不清楚'},
                {"op": 2, "content": '喜操纵：精明处事，操纵事情，使对自己有利'},
            ),
            (
                {"op": 2, "content": '缓慢：行动思想均比较慢，过分麻烦'},
                {"op": 3, "content": '顽固：决心依自己的意愿行事，不易被说服'},
                {"op": 1, "content": '好表现：要吸引人，需要自己成为被人注意的中心'},
                {"op": 4, "content": '有戒心：不易相信，对语言背后的真正的动机存在疑问'},
            ),
            (
                {"op": 2, "content": '孤僻：需要大量的时间独处，避开人群'},
                {"op": 4, "content": '统治欲：毫不犹豫地表示自己的正确或控制能力'},
                {"op": 3, "content": '懒惰：总是先估量事情要耗费多少精力，能不做最好'},
                {"op": 1, "content": '大嗓门：说话声和笑声总盖过他人'},
            ),
            (
                {"op": 3, "content": '拖延：凡事起步慢，需要推动力'},
                {"op": 4, "content": '多疑：凡事怀疑，不相信别人'},
                {"op": 1, "content": '易怒：对行动不快或不能完成指定工作时易烦躁和发怒'},
                {"op": 2, "content": '不专注：无法专心致志或者集中精力'},
            ),
            (
                {"op": 4, "content": '报复性：记恨并惩罚冒犯自己的人'},
                {"op": 2, "content": '烦躁：喜新厌旧，不喜欢长时间做相同的事情'},
                {"op": 3, "content": '勉强：不愿意参与或者说投入'},
                {"op": 1, "content": '轻率：因没有耐心，不经思考，草率行动'},
            ),
            (
                {"op": 3, "content": '妥协：为避免矛盾即使自己是对的也不惜放弃自己的立场'},
                {"op": 4, "content": '好批评：不断地衡量和下判断，经常考虑提出反对意见'},
                {"op": 1, "content": '狡猾：精明，总是有办法达到目的'},
                {"op": 2, "content": '善变：像孩子般注意力短暂，需要各种变化，怕无聊'},
            ),
        )
        return Response(data)

    data = {
        'username': request.POST.get('username'),
        'op0': request.POST.get('op0'),
        'op1': request.POST.get('op1'),
        'op2': request.POST.get('op2'),
        'op3': request.POST.get('op3'),
        'op4': request.POST.get('op4'),
        'op5': request.POST.get('op5'),
        'op6': request.POST.get('op6'),
        'op7': request.POST.get('op7'),
        'op8': request.POST.get('op8'),
        'op9': request.POST.get('op9'),
        'op10': request.POST.get('op10'),
        'op11': request.POST.get('op11'),
        'op12': request.POST.get('op12'),
        'op13': request.POST.get('op13'),
        'op14': request.POST.get('op14'),
        'op15': request.POST.get('op15'),
        'op16': request.POST.get('op16'),
        'op17': request.POST.get('op17'),
        'op18': request.POST.get('op18'),
        'op19': request.POST.get('op19'),
        'op20': request.POST.get('op20'),
        'op21': request.POST.get('op21'),
        'op22': request.POST.get('op22'),
        'op23': request.POST.get('op23'),
        'op24': request.POST.get('op24'),
        'op25': request.POST.get('op25'),
        'op26': request.POST.get('op26'),
        'op27': request.POST.get('op27'),
        'op28': request.POST.get('op28'),
        'op29': request.POST.get('op29'),
        'op30': request.POST.get('op30'),
        'op31': request.POST.get('op31'),
        'op32': request.POST.get('op32'),
        'op33': request.POST.get('op33'),
        'op34': request.POST.get('op34'),
        'op35': request.POST.get('op35'),
        'op36': request.POST.get('op36'),
        'op37': request.POST.get('op37'),
        'op38': request.POST.get('op38'),
        'op39': request.POST.get('op39'),
    }

    for i in data:
        if (data[i] == None):
            print('err')
            return Response("err")
    data = {
        'username': eval(request.POST.get('username')),
        'op0': int(request.POST.get('op0')),
        'op1': int(request.POST.get('op1')),
        'op2': int(request.POST.get('op2')),
        'op3': int(request.POST.get('op3')),
        'op4': int(request.POST.get('op4')),
        'op5': int(request.POST.get('op5')),
        'op6': int(request.POST.get('op6')),
        'op7': int(request.POST.get('op7')),
        'op8': int(request.POST.get('op8')),
        'op9': int(request.POST.get('op9')),
        'op10': int(request.POST.get('op10')),
        'op11': int(request.POST.get('op11')),
        'op12': int(request.POST.get('op12')),
        'op13': int(request.POST.get('op13')),
        'op14': int(request.POST.get('op14')),
        'op15': int(request.POST.get('op15')),
        'op16': int(request.POST.get('op16')),
        'op17': int(request.POST.get('op17')),
        'op18': int(request.POST.get('op18')),
        'op19': int(request.POST.get('op19')),
        'op20': int(request.POST.get('op20')),
        'op21': int(request.POST.get('op21')),
        'op22': int(request.POST.get('op22')),
        'op23': int(request.POST.get('op23')),
        'op24': int(request.POST.get('op24')),
        'op25': int(request.POST.get('op25')),
        'op26': int(request.POST.get('op26')),
        'op27': int(request.POST.get('op27')),
        'op28': int(request.POST.get('op28')),
        'op29': int(request.POST.get('op29')),
        'op30': int(request.POST.get('op30')),
        'op31': int(request.POST.get('op31')),
        'op32': int(request.POST.get('op32')),
        'op33': int(request.POST.get('op33')),
        'op34': int(request.POST.get('op34')),
        'op35': int(request.POST.get('op35')),
        'op36': int(request.POST.get('op36')),
        'op37': int(request.POST.get('op37')),
        'op38': int(request.POST.get('op38')),
        'op39': int(request.POST.get('op39')),
    }
    print(data)
    if (Disc.objects.filter(username=data['username']).first() == None):
        Disc.objects.create(username=data['username'])
    Disc.objects.filter(username=data['username']).update(**data)
    return Response('ok')


@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4', 'GET'])
def DiscTest(request):
    username = request.POST.get('username')
    username = eval(username)
    row_object = Disc.objects.filter(username=username).values().first()
    a = 0
    b = 0
    c = 0
    d = 0
    for i in row_object:
        if row_object[i] == 1:
            a += 1
        if row_object[i] == 2:
            b += 1
        if row_object[i] == 3:
            c += 1
        if row_object[i] == 4:
            d += 1
    if a > 10:
        return Response({'a': "高 D 型特质的人可以称为是“天生的领袖”。",
                         'b': "在情感方面，D型人一个坚定果敢的人，酷好变化，喜欢控制，干劲十足，独立自主，超级自信。可是，由于比较不会顾及别人的感受，所以显得粗鲁、霸道、没有耐心、穷追不舍、不会放松。D型人不习惯与别人进行感情上的交流，不会恭维人，不喜欢眼泪，匮乏同情心。 ",
                         'c': "在工作方面，D型人是一个务实和讲究效率的人，目标明确，眼光全面，组织力强，行动迅速，解决问题不过夜，果敢坚持到底，在反对声中成长。但是，因为过于强调结果， D型人往往容易忽视细节，处理问题不够细致。爱管人、喜欢支使他人的特点使得D型人能够带动团队进步，但也容易激起同事的反感。",
                         'd': "在人际关系方面， D型人喜欢为别人做主，虽然这样能够帮助别人做出选择，但也容易让人有强迫感。由于关注自己的目标， D型人在乎的是别人的可利用价值。喜欢控制别人，不会说对不起。",
                         'e': "积级进取、争强好胜、强势、爱追根究底、直截了当、主动的开拓者、坚持意见、自信、直率",
                         'f': "高 D 型特质的人"})
    if b > 10:
        return Response({a: "高 I 型的人通常是较为活泼的团队活动组织者",
                         'b': "I 型人是一个情感丰富而外露的人，由于性格活跃，爱说，爱讲故事，幽默，彩色记忆，能抓住听众，你常常是聚会的中心人物。是一个天才的演员，天真无邪，热情诚挚，喜欢送礼和接受礼物，看重人缘。情绪化的特点使得你容易兴奋，喜欢吹牛、说大话，天真，永远长不大，富有喜剧色彩。但是，似乎也很容易生气，爱抱怨，大嗓门，不成熟。",
                         'c': "在工作方面，I型人是一个热情的推动者，总有新主意，色彩丰富，说干就干，能够鼓励和带领他人一起积极投入工作。可是，I型人似乎总是情绪决定一切，想哪儿说哪儿，而且说得多干得少，遇到困难容易失去信心，杂乱无章，做事不彻底，爱走神儿，爱找借口。喜欢轻松友好的环境，非常害怕被拒绝。",
                         'd': "在人际关系方面，I型人容易交上朋友，朋友也多。关爱朋友，也被朋友称赞。爱当主角，爱受欢迎喜欢控制谈话内容。可是，喜欢即兴表演的特点使得I型人常常不能仔细理解别人，而且健忘多变。",
                         'e': "有影响力、有说服力、友好、善于言辞、健谈、乐观积极、善于交际",
                         'f': "高 I 型特质的人"})
    if c > 10:
        return Response({"a": "高 S 型的人通常较为平和，知足常乐，不愿意主动前进",
                         "b": "在情感方面，S型人是一个温和主义者，悠闲，平和，有耐心，感情内藏，待人和蔼，乐于倾听，遇事冷静，随遇而安。 S型喜欢使用一句口头禅：“不过如此。”这个特点使得S型总是缺乏热情，不愿改变。",
                         "c": "在工作方面， S型能够按部就班地管理事务，胜任工作并能够持之以恒。奉行中庸之道，平和可亲，一方面习惯于避免冲突，另一方面也能处变不惊。但是， S型似乎总是慢吞吞的，很难被鼓动，懒惰，马虎，得过且过。由于害怕承担风险和责任，宁愿站在一边旁观。很多时候， S型总是焉有主意，有话不说，或折衷处理。 ",
                         "d": "在人际关系方面， S型是一个容易相处的人，喜欢观察人、琢磨人，乐于倾听，愿意支持。可是，由于不以为然， S型也可能显得漠不关心，或者嘲讽别人。",
                         "e": "可靠、深思熟虑、亲切友好、有毅力、坚持不懈、善倾听者、全面周到、自制力强",
                         'f': "高 S 型特质的人"})
    if d > 10:
        return Response({"a": "高 C 型的人通常是喜欢追求完美的专业型人才",
                         "b": "在情感方面，C型人是一个性格深沉的人，严肃认真，目的性强，善于分析，愿意思考人生与工作的意义，喜欢美丽，对他人敏感，理想主义。但是， C型人总是习惯于记住负面的东西，容易情绪低落，过分自我反省，自我贬低，离群索居，有忧郁症倾向。",
                         "c": "在工作方面， C型人是一个完美主义者，高标准，计划性强，注重细节，讲究条理，整洁，能够发现问题并制订解决问题的办法，喜欢图表和清单，坚持己见，善始善终。但是， C型人也很可能是一个优柔寡断的人，习惯于收集信息资料和做分析，却很难投入到实际运作的工作中来。容易自我否定，因此需要别人的认同。同时，也习惯于挑剔别人，不能忍受别人的工作做不好。",
                         "d": "对待人际关系方面， C型人一方面在寻找理想伙伴，另一方面却交友谨慎。能够深切地关怀他人，善于倾听抱怨，帮助别人解决困难。但是， C型人似乎始终有一种不安全感，以致于感情内向，退缩，怀疑别人，喜欢批评人事，却不喜欢别人的反对。",
                         "e": "遵从、仔细、有条不紊、严谨、准确、完美主义者、逻辑性强",
                         'f': "高 C 型特质的人"})
    return Response('ok')
