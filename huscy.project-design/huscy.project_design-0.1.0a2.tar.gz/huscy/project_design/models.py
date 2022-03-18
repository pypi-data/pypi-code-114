from datetime import timedelta
from enum import Enum

from django.conf import settings
from django.db import models

from huscy.projects.models import Project


class Experiment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='experiments')

    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, default='')

    order = models.PositiveSmallIntegerField()


class Session(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name='sessions')
    title = models.CharField(max_length=64)
    order = models.PositiveSmallIntegerField()

    setup_time = models.DurationField(default=timedelta())
    duration = models.DurationField()
    teardown_time = models.DurationField(default=timedelta())

    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    max_number_of_participants = models.PositiveIntegerField(default=1)


class Stimulus(models.Model):
    class TYPE(Enum):
        auditive = (0, 'auditive')
        gustatory = (1, 'gustatory')
        haptic = (2, 'haptic')
        olfactory = (3, 'olfactory')
        visual = (4, 'visual')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    type = models.PositiveSmallIntegerField(choices=[x.value for x in TYPE])


class DataAcquisitionMethod(models.Model):
    class TYPE(Enum):
        behavioral = ('behav', 'Behavioral')
        biological = ('bio', 'Biological samples')
        eeg = ('eeg', 'Electroencephalography')
        meg = ('meg', 'Magnetoencephalography')
        microscopy = ('micro', 'Microscopy data')
        mri = ('mri', 'Magnetic resonance imaging')
        nirs = ('nirs', 'Near-Infrared Spectroscopy')
        pause = ('pause', 'Pause')
        pet = ('pet', 'Positron-emission tomography')
        physiological = ('phys', 'Physiological measures')
        questionnaire = ('quest', 'Questionnaire')
        screening = ('screen', 'Screening')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    stimulus = models.ForeignKey(Stimulus, on_delete=models.SET_NULL, null=True)

    type = models.CharField(max_length=16, choices=[x.value for x in TYPE])

    location = models.CharField(max_length=126)


class Behavioral(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE,
                               related_name='behaviorals')


class Biological(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE,
                               related_name='biologicals')


class EEG(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE, related_name='eeg')


class MEG(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE, related_name='meg')


class Microscopy(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE,
                               related_name='microscopys')


class MRI(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE, related_name='mri')


class NIRS(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE, related_name='nirs')


class Pause(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE,
                               related_name='pause')


class PET(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE, related_name='pet')


class Physiological(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE,
                               related_name='physiologicals')


class Questionnaire(models.Model):
    def get_upload_path(self, filename):
        return f'projects/data_acquisition_methods/questionnaires/{filename}'

    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE,
                               related_name='questionnaires')

    filehandle = models.FileField(upload_to=get_upload_path)
    filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True, editable=False)
    uploaded_by = models.CharField(max_length=128, editable=False)


class Screening(models.Model):
    method = models.ForeignKey(DataAcquisitionMethod, on_delete=models.CASCADE,
                               related_name='screenings')
