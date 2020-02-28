from django.db import models


class Item(models.Model):
    CATEGORIES = {
        ('General Medical Equipment and Supplies', 'General Medical Equipment and Supplies'),
        ('Anaesthesiology', 'Anaesthesiology'),
        ('Apparel', 'Apparel'),
        ('Cardiology', 'Cardiology'),
        ('Dental E0quipment and Supplies', 'Dental Equipment and Supplies'),
        ('Gynecology & Urology', 'Gynecology & Urology'),
        ('Laboratory', 'Laboratory'),
        ('Nephrology', 'Nephrology'),
        ('Neurology', 'Neurology'),
        ('Obstetrics and Maternity Care', 'Obstetrics and Maternity Care'),
        ('Ophthalmology and Optometry', 'Ophthalmology and Optometry'),
        ('Otology and Neurotology', 'Otology and Neurotology'),
        ('Physical and Occupational Therapy', 'Physical and Occupational Therapy'),
        ('Radiology', 'Radiology'),
        ('Sterilization', 'Sterilization'),
        ('Surgery', 'Surgery'),
    }

    name = models.CharField(max_length=100, null=True, unique=True)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100, null=True, choices=CATEGORIES)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Drug(models.Model):
    CATEGORY = (
        ('Adamantane Antivirals', 'Adamantane Antivirals'),
        ('Adrenal Cortical Steroids', 'Adrenal Cortical Steroids'),
        ('Adrenal Corticosteroid Inhibitors', 'Adrenal Corticosteroid Inhibitors'),
        ('Allergenics', 'Allergenics'),
        ('Amebicides', 'Amebicides'),
        ('Analgesics', 'Analgesics'),
        ('Barbiturates', 'Barbiturates'),
        ('Biologicals', 'Biologicals'),
        ('Bronchodilators', 'Bronchodilators'),
        ('Calcimimetics', 'Calcimimetics'),
        ('Calcitonin', 'Calcitonin'),
        ('Catecholamines', 'Catecholamines'),
        ('Cephalosporins', 'Cephalosporins'),
        ('Coagulation Modifiers', 'Coagulation Modifiers'),
        ('Decongestants', 'Decongestants'),
        ('Diarylquinolines', 'Diarylquinolines'),
        ('Diuretics', 'Diuretics'),
        ('Echinocandins', 'Echinocandins'),
        ('Estrogens', 'Estrogens'),
        ('Fibric Acid Derivatives', 'Fibric Acid Derivatives'),
        ('Gallstone Solubilizing Agents', 'Gallstone Solubilizing Agents'),
        ('Glucocorticoids', 'Glucocorticoids'),
        ('Glycylcyclines', 'Glycylcyclines'),
        ('Gonadotropins', 'Gonadotropins'),
        ('H2 Antagonists', 'H2 Antagonists'),
        ('Heparins', 'Heparins'),
        ('Illicit', 'Illicit'),
        ('Insulin', 'Insulin'),
        ('Interferons', 'Interferons'),
        ('Interleukins', 'Interleukins'),
        ('Iodinated Contrast Media', 'Iodinated Contrast Media'),
        ('Iron Products', 'Iron Products'),
        ('Ketolides', 'Ketolides'),
        ('Laxatives', 'Laxatives'),
    )

    name = models.CharField(max_length=100, null=True, unique=True)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    date_updated = models.DateField(auto_now_add=True)
    genericName = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name + '-' + self.genericName