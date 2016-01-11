from django.shortcuts import render, redirect
from common.views import ProtectedView
from cartograph.forms import RaidModelForm
from cartograph.models import Raid


class HomeView(ProtectedView):
    def get(self, request):
        context = {'raids': Raid.objects.all()}
        return render(request, 'dashboard/home.html', context)
home = HomeView.as_view()


class RaidsAdd(ProtectedView):
    def get(self, request):
        context = {"form": RaidModelForm(reportee=request.user.member)}
        return render(request, 'dashboard/raids/add.html', context)

    def post(self, request):
        if not hasattr(request.user, 'member'):
            return redirect('dashboard:home')
        form = RaidModelForm(request.POST, reportee=request.user.member)
        if form.is_valid():
            raid = form.save()
            return render(request, 'dashboard:raid_created')
        else:
            context = {'form': form}
            return render(request, 'dashboard/raids/add.html', context)
raids_add = RaidsAdd.as_view()


class RaidsEdit(ProtectedView):
    def get(self, request, raid_id):
        raid = Raid.objects.get(id=raid_id)
        form = RaidModelForm(instance=raid, reportee=request.user.member)
        context = {'raid': raid, 'form': form}
        return render(request, 'dashboard/raids/edit.html', context)

    def post(self, request, raid_id):
        raid = Raid.objects.get(id=raid_id)
        form = RaidModelForm(request.POST, instance=raid, reportee=request.user.member)
        if form.is_valid():
            form.save()
            return redirect('dashboard:raids_mine')
        print 'form is not valid'
        print form.errors
        context = {'raid': raid, 'form': form}
        return render(request, 'dashboard/raids/edit.html', context)

raids_edit = RaidsEdit.as_view()


class RaidsMine(ProtectedView):
    def get(self, request):
        raids = Raid.objects.filter(reportee=request.user.member)
        return render(request, 'dashboard/raids/mine.html', {'raids': raids})
raids_mine = RaidsMine.as_view()