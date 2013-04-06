from thestar.models import Competitor
def create_competitor():
    kangsom, created = Competitor.objects.get_or_create(name='Tanatat Chaiyaat', nick_name='Kangsom', no=8)

    return kangsom