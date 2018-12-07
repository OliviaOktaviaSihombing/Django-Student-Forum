import datetime

from channels import Group
import json
from .models import t_topik, t_komentar, t_user


# Connected to websocket.connect
def ws_add(message):
    message.reply_channel.send({"accept": True})
    grup = message.content['path']
    grup = ''.join(str(ord(c)) for c in grup)
    Group(grup).add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    grup = message.content['path']
    grup = ''.join(str(ord(c)) for c in grup)
    data = json.loads(message.content['text'])
    user = t_user.objects.get(pk=data['email'])
    topik = t_topik.objects.get(pk=data['id_topik'])
    komentar = t_komentar(email=user, id_topik=topik, isi_komentar=data['isi_komentar'])
    komentar.save()
    jumlah_komen = t_komentar.objects.filter(id_topik = topik)
    topik.jumlah_komentar_topik = len(jumlah_komen)
    topik.save()
    t = datetime.datetime.now()
    date = t.strftime('%B')+" "+str(t.day)+" "+str(t.year)
    content = {
        'date': date,
        'avatar': user.avatar_user,
        'name': user.full_name,
        'komentar': komentar.isi_komentar,
        'email': user.email,
        'jumlah_komen': topik.jumlah_komentar_topik
    }
    Group(grup).send({
        # "text": json.dumps(data)
        "text": json.dumps(content)
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    grup = message.content['path']
    grup = ''.join(str(ord(c)) for c in grup)
    Group(grup).discard(message.reply_channel)