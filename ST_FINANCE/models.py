# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_number = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=30, blank=True, null=True)
    labor_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Accruals(models.Model):
    pr_number = models.CharField(max_length=11, blank=True, null=True)
    transaction_id = models.IntegerField(blank=True, null=True)
    quarter = models.CharField(max_length=4, blank=True, null=True)
    accrued = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pending = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accruals'


class Actions(models.Model):
    action_id = models.AutoField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    owner = models.CharField(max_length=64, blank=True, null=True)
    action = models.CharField(max_length=800)
    open_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=800, blank=True, null=True)
    state = models.CharField(max_length=20)
    power = models.CharField(max_length=12, blank=True, null=True)
    emc = models.CharField(max_length=12, blank=True, null=True)
    thermal = models.CharField(max_length=12, blank=True, null=True)
    mech = models.CharField(max_length=12, blank=True, null=True)
    telecom = models.CharField(max_length=12, blank=True, null=True)
    safety = models.CharField(max_length=12, blank=True, null=True)
    radio = models.CharField(max_length=12, blank=True, null=True)
    nebs = models.CharField(max_length=12, blank=True, null=True)
    reliability = models.CharField(max_length=12, blank=True, null=True)
    pcb_tools = models.CharField(max_length=12, blank=True, null=True)
    hw_lab = models.CharField(max_length=12, blank=True, null=True)
    si = models.CharField(max_length=12, blank=True, null=True)
    pgm = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions'


class AsicFamilies(models.Model):
    family_id = models.AutoField(primary_key=True)
    family = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asic_families'


class AsicUtilization(models.Model):
    asic_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asic_utilization'


class Asics(models.Model):
    asic_id = models.AutoField(primary_key=True)
    chip = models.CharField(max_length=10, blank=True, null=True)
    family_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asics'


class BgList(models.Model):
    bg_id = models.AutoField(primary_key=True)
    bg = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bg_list'


class BuList(models.Model):
    bu_id = models.AutoField(primary_key=True)
    bu = models.CharField(max_length=20, blank=True, null=True)
    bg_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bu_list'


class Budget(models.Model):
    account_id = models.IntegerField(blank=True, null=True)
    function_id = models.IntegerField(blank=True, null=True)
    project_type_id = models.IntegerField(blank=True, null=True)
    bu_id = models.IntegerField(blank=True, null=True)
    labor_type_id = models.IntegerField(blank=True, null=True)
    quarter = models.CharField(max_length=4, blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget'
        unique_together = (('account_id', 'function_id', 'project_type_id', 'bu_id', 'labor_type_id', 'quarter'),)


class BudgetTracker(models.Model):
    id = models.IntegerField()
    bu_id = models.IntegerField()
    quarter = models.CharField(max_length=24)
    xq = models.CharField(db_column='xQ', max_length=24)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'budget_tracker'


class BudgetTrackerOld(models.Model):
    function = models.CharField(db_column='Function', max_length=13, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=14, blank=True, null=True)  # Field name made lowercase.
    bg = models.CharField(db_column='BG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    bu = models.CharField(db_column='BU', max_length=9, blank=True, null=True)  # Field name made lowercase.
    labor = models.CharField(db_column='Labor', max_length=11, blank=True, null=True)  # Field name made lowercase.
    total = models.CharField(db_column='Total', max_length=13, blank=True, null=True)  # Field name made lowercase.
    quarter = models.CharField(db_column='Quarter', max_length=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'budget_tracker_old'


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'categories'


class ClarityData(models.Model):
    project_type = models.CharField(max_length=45)
    npi_project_type = models.CharField(max_length=10)
    dependency = models.IntegerField(blank=True, null=True)
    dimid = models.CharField(max_length=50, blank=True, null=True)
    prjcode = models.CharField(max_length=20, blank=True, null=True)
    prjintid = models.IntegerField(blank=True, null=True)
    prjname = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=7, blank=True, null=True)
    bu = models.CharField(max_length=200, blank=True, null=True)
    current_phase = models.CharField(max_length=50, blank=True, null=True)
    milestone_rev_date = models.CharField(max_length=32, blank=True, null=True)
    milestone_plan_date = models.CharField(max_length=32, blank=True, null=True)
    next_exit_date = models.DateField(blank=True, null=True)
    release_target = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=800, blank=True, null=True)
    status_comment = models.CharField(max_length=800, blank=True, null=True)
    lifecycle_status = models.CharField(max_length=200)
    fundingstatus = models.CharField(max_length=200)
    p0exitplan = models.DateField(blank=True, null=True)
    p0exitrev = models.DateField(blank=True, null=True)
    p0exitactual = models.DateField(blank=True, null=True)
    bu_p0exit_date = models.DateField(blank=True, null=True)
    p1exitplan = models.DateField(blank=True, null=True)
    p1exitrev = models.DateField(blank=True, null=True)
    p1exitactual = models.DateField(blank=True, null=True)
    bu_p1exit_date = models.DateField(blank=True, null=True)
    p2exitplan = models.DateField(blank=True, null=True)
    p2exitrev = models.DateField(blank=True, null=True)
    p2exitactual = models.DateField(blank=True, null=True)
    bu_p2exit_date = models.DateField(blank=True, null=True)
    p3exitplan = models.DateField(blank=True, null=True)
    p3exitrev = models.DateField(blank=True, null=True)
    p3exitactual = models.DateField(blank=True, null=True)
    bu_p3exit_date = models.DateField(blank=True, null=True)
    p4exitplan = models.DateField(blank=True, null=True)
    p4exitrev = models.DateField(blank=True, null=True)
    p4exitactual = models.DateField(blank=True, null=True)
    bu_p4exit_date = models.DateField(blank=True, null=True)
    plm = models.CharField(max_length=32, blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clarity_data'


class Components(models.Model):
    component_id = models.AutoField(primary_key=True)
    component = models.CharField(max_length=120, blank=True, null=True)
    component_type = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    part_number = models.CharField(max_length=20, blank=True, null=True)
    vendor_pn = models.CharField(max_length=20, blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    new_component = models.CharField(max_length=1, blank=True, null=True)
    status_ryg = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    impact = models.CharField(max_length=128, blank=True, null=True)
    fix = models.CharField(max_length=128, blank=True, null=True)
    chassis_1 = models.CharField(max_length=20, blank=True, null=True)
    chassis_2 = models.CharField(max_length=20, blank=True, null=True)
    chassis_3 = models.CharField(max_length=20, blank=True, null=True)
    chassis_4 = models.CharField(max_length=20, blank=True, null=True)
    chassis_5 = models.CharField(max_length=20, blank=True, null=True)
    chassis_6 = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=20, blank=True, null=True)
    proto_1a_date = models.DateField(blank=True, null=True)
    proto_1b_date = models.DateField(blank=True, null=True)
    proto_2a_date = models.DateField(blank=True, null=True)
    proto_2b_date = models.DateField(blank=True, null=True)
    proto_3a_date = models.DateField(blank=True, null=True)
    proto_3b_date = models.DateField(blank=True, null=True)
    vendor = models.CharField(max_length=20, blank=True, null=True)
    pilot_hw_available = models.DateField(blank=True, null=True)
    dev_complete_hw_available = models.DateField(blank=True, null=True)
    ps_safety_certs_vendor = models.DateField(blank=True, null=True)
    frs_quantity = models.IntegerField(blank=True, null=True)
    proto_1a_prev_date = models.DateField(blank=True, null=True)
    proto_1a_chg_date = models.DateField(blank=True, null=True)
    proto_1a_comment = models.CharField(max_length=40, blank=True, null=True)
    proto_1b_prev_date = models.DateField(blank=True, null=True)
    proto_1b_chg_date = models.DateField(blank=True, null=True)
    proto_1b_comment = models.CharField(max_length=40, blank=True, null=True)
    proto_2a_prev_date = models.DateField(blank=True, null=True)
    proto_2a_chg_date = models.DateField(blank=True, null=True)
    proto_2a_comment = models.CharField(max_length=40, blank=True, null=True)
    proto_2b_prev_date = models.DateField(blank=True, null=True)
    proto_2b_chg_date = models.DateField(blank=True, null=True)
    proto_2b_comment = models.CharField(max_length=40, blank=True, null=True)
    proto_3a_prev_date = models.DateField(blank=True, null=True)
    proto_3a_chg_date = models.DateField(blank=True, null=True)
    proto_3a_comment = models.CharField(max_length=40, blank=True, null=True)
    proto_3b_prev_date = models.DateField(blank=True, null=True)
    proto_3b_chg_date = models.DateField(blank=True, null=True)
    proto_3b_comment = models.CharField(max_length=40, blank=True, null=True)
    p1a_ryg = models.CharField(max_length=20, blank=True, null=True)
    p1b_ryg = models.CharField(max_length=20, blank=True, null=True)
    p2a_ryg = models.CharField(max_length=20, blank=True, null=True)
    p2b_ryg = models.CharField(max_length=20, blank=True, null=True)
    p3a_ryg = models.CharField(max_length=20, blank=True, null=True)
    p3b_ryg = models.CharField(max_length=20, blank=True, null=True)
    ps_safety_ryg = models.CharField(max_length=20, blank=True, null=True)
    dev_complete_hw_avail_ryg = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'components'


class Content(models.Model):
    page = models.CharField(max_length=20)
    tabnum = models.IntegerField(blank=True, null=True)
    tabname = models.CharField(max_length=24, blank=True, null=True)
    enabled = models.IntegerField()
    contentlink = models.CharField(db_column='contentLink', max_length=200, blank=True, null=True)  # Field name made lowercase.
    conent_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content'


class ContractorTracker(models.Model):
    name = models.CharField(max_length=64)
    vendor = models.CharField(max_length=64)
    geo_id = models.IntegerField(blank=True, null=True)
    manager = models.CharField(max_length=32, blank=True, null=True)
    function_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    rate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    qtr_rate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    comments = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contractor_tracker'


class Engops(models.Model):
    type = models.CharField(max_length=12)
    item = models.CharField(max_length=480)
    owner = models.CharField(max_length=24, blank=True, null=True)
    priority = models.CharField(max_length=12)
    open_date = models.DateField()
    close_date = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=12)
    status = models.CharField(max_length=480, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engops'


class FinanceGroups(models.Model):
    finance_group = models.CharField(max_length=22)

    class Meta:
        managed = False
        db_table = 'finance_groups'


class Forecasts(models.Model):
    function_id = models.IntegerField(blank=True, null=True)
    project_type_id = models.IntegerField(blank=True, null=True)
    bu_id = models.IntegerField(blank=True, null=True)
    labor_type_id = models.IntegerField(blank=True, null=True)
    quarter = models.CharField(max_length=4, blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forecasts'
        unique_together = (('function_id', 'project_type_id', 'bu_id', 'labor_type_id', 'quarter'),)


class Frs(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    frs = models.DateField(blank=True, null=True)
    rev = models.IntegerField(blank=True, null=True)
    chg = models.DateField(blank=True, null=True)
    reason = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frs'


class Functions(models.Model):
    function_id = models.AutoField(primary_key=True)
    function = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'functions'


class Geography(models.Model):
    geo_id = models.AutoField(primary_key=True)
    geography = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=20)
    labor_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geography'


class Homologation(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    percent_complete = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=240, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homologation'


class Improvements(models.Model):
    type = models.CharField(max_length=12)
    item = models.CharField(max_length=480)
    priority = models.CharField(max_length=12)
    requester = models.CharField(max_length=32, blank=True, null=True)
    open_date = models.DateField()
    close_date = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=12)
    status = models.CharField(max_length=480, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'improvements'


class LaborAllocations(models.Model):
    function_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    resource_id = models.IntegerField(blank=True, null=True)
    component_id = models.IntegerField()
    activity = models.CharField(max_length=80, blank=True, null=True)
    quarter = models.CharField(max_length=4, blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated')  # Field name made lowercase.
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labor_allocations'
        unique_together = (('function_id', 'project_id', 'resource_id', 'component_id', 'activity', 'quarter'),)


class LaborAllocationsScript(models.Model):
    labor_allocation_id = models.IntegerField(blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated', blank=True, null=True)  # Field name made lowercase.
    old_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    new_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    approved = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labor_allocations_script'


class LaborTypes(models.Model):
    labor_type_id = models.AutoField(primary_key=True)
    labor_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labor_types'


class Milestones(models.Model):
    milestone_id = models.AutoField(primary_key=True)
    transaction_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    milestone = models.CharField(max_length=128, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    function_id = models.IntegerField(blank=True, null=True)
    subfunction = models.CharField(max_length=32, blank=True, null=True)
    bu_dependency = models.CharField(max_length=40, blank=True, null=True)
    bu_commit_date = models.DateField(blank=True, null=True)
    bu_actual_date = models.DateField(blank=True, null=True)
    deliverable = models.CharField(max_length=40, blank=True, null=True)
    st_commit_date = models.DateField(blank=True, null=True)
    st_actual_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'milestones'


class NebsTracker(models.Model):
    state = models.CharField(max_length=22, blank=True, null=True)
    bu = models.CharField(max_length=128, blank=True, null=True)
    program = models.CharField(max_length=256, blank=True, null=True)
    stage = models.CharField(max_length=32, blank=True, null=True)
    comments = models.CharField(max_length=8192, blank=True, null=True)
    frs = models.DateField(blank=True, null=True)
    hw_receive_eta = models.DateField(blank=True, null=True)
    hw_receive_actual = models.DateField(blank=True, null=True)
    loc_etc = models.DateField(blank=True, null=True)
    loc_actual = models.DateField(blank=True, null=True)
    report_etc = models.DateField(blank=True, null=True)
    report_actual = models.DateField(blank=True, null=True)
    standard = models.CharField(max_length=128, blank=True, null=True)
    test_lab = models.CharField(max_length=20, blank=True, null=True)
    platform = models.CharField(max_length=256, blank=True, null=True)
    sw_release = models.CharField(max_length=128, blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nebs_tracker'


class OemProjectStages(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    oem_initial_scoping = models.DateField(blank=True, null=True)
    oem_initial_scoping_progress = models.IntegerField(blank=True, null=True)
    oem_scoping_comment = models.CharField(max_length=60, blank=True, null=True)
    oem_power_testing_ibm = models.DateField(blank=True, null=True)
    oem_power_testing_progress = models.CharField(max_length=60, blank=True, null=True)
    oem_power_comment = models.CharField(max_length=60, blank=True, null=True)
    oem_power_cord_spec_dell = models.DateField(blank=True, null=True)
    oem_power_cord_progress = models.CharField(max_length=60, blank=True, null=True)
    oem_power_cord_comment = models.CharField(max_length=300, blank=True, null=True)
    oem_emc = models.DateField(blank=True, null=True)
    oem_emc_progress = models.IntegerField(blank=True, null=True)
    oem_emc_comment = models.CharField(max_length=300, blank=True, null=True)
    oem_safety = models.DateField(blank=True, null=True)
    oem_safety_progress = models.IntegerField(blank=True, null=True)
    oem_safety_comment = models.CharField(max_length=300, blank=True, null=True)
    oem_labels = models.DateField(blank=True, null=True)
    oem_labels_progress = models.IntegerField(blank=True, null=True)
    oem_labels_comment = models.CharField(max_length=300, blank=True, null=True)
    oem_nebs = models.DateField(blank=True, null=True)
    oem_nebs_progress = models.IntegerField(blank=True, null=True)
    oem_nebs_comment = models.CharField(max_length=300, blank=True, null=True)
    oem_epd = models.DateField(blank=True, null=True)
    oem_epd_progress = models.IntegerField(blank=True, null=True)
    oem_epd_comment = models.CharField(max_length=300, blank=True, null=True)
    oem_frs = models.DateField(blank=True, null=True)
    oem_frs_progress = models.IntegerField(blank=True, null=True)
    oem_frs_comment = models.CharField(max_length=300, blank=True, null=True)
    oem_description = models.CharField(max_length=300, blank=True, null=True)
    oem_status = models.CharField(max_length=300, blank=True, null=True)
    second_edition_safety = models.DateField(blank=True, null=True)
    second_edition_safety_progress = models.IntegerField(blank=True, null=True)
    second_edition_comment = models.CharField(max_length=300, blank=True, null=True)
    oem_homologation_detail = models.CharField(max_length=300, blank=True, null=True)
    partner = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oem_project_stages'


class PoTransactions(models.Model):
    pot_id = models.AutoField(primary_key=True)
    pr_number = models.IntegerField()
    transaction_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'po_transactions'


class PowerProjectSchedules(models.Model):
    sch_id = models.AutoField(primary_key=True)
    pwr_proj_id = models.IntegerField()
    sch_type = models.CharField(max_length=12, blank=True, null=True)
    spec_complete = models.DateField(blank=True, null=True)
    spec_comment = models.CharField(max_length=32, blank=True, null=True)
    proto1_date = models.DateField(blank=True, null=True)
    proto1_comment = models.CharField(max_length=32, blank=True, null=True)
    proto1b_date = models.DateField(blank=True, null=True)
    proto1b_comment = models.CharField(max_length=32, blank=True, null=True)
    proto2_date = models.DateField(blank=True, null=True)
    proto2_comment = models.CharField(max_length=32, blank=True, null=True)
    qe_start = models.DateField(blank=True, null=True)
    qe_complete = models.DateField(blank=True, null=True)
    safety_start = models.DateField(blank=True, null=True)
    safety_tier1_complete = models.DateField(blank=True, null=True)
    safety_all_complete = models.DateField(blank=True, null=True)
    pilot_date = models.DateField(blank=True, null=True)
    pilot_comment = models.CharField(max_length=32, blank=True, null=True)
    production_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'power_project_schedules'


class PowerProjects(models.Model):
    project_id = models.IntegerField()
    pwr_project = models.CharField(max_length=40)
    pwr_active = models.CharField(max_length=1)
    status = models.CharField(max_length=2000, blank=True, null=True)
    stage = models.CharField(max_length=40, blank=True, null=True)
    vendor = models.CharField(max_length=64, blank=True, null=True)
    pwr_description = models.CharField(max_length=200, blank=True, null=True)
    eighty_plus = models.CharField(max_length=80, blank=True, null=True)
    jnpr_pn = models.CharField(max_length=100, blank=True, null=True)
    jnpr_model = models.CharField(max_length=32, blank=True, null=True)
    vendor_pn = models.CharField(max_length=40, blank=True, null=True)
    jots = models.CharField(max_length=20, blank=True, null=True)
    pwr_eng = models.CharField(max_length=40, blank=True, null=True)
    vendor_pgm = models.CharField(max_length=32, blank=True, null=True)
    spec = models.DateField(blank=True, null=True)
    rfq = models.DateField(blank=True, null=True)
    award_date = models.DateField(blank=True, null=True)
    review_quality = models.DateField(blank=True, null=True)
    review_mech = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'power_projects'


class Programs(models.Model):
    program_id = models.AutoField(primary_key=True)
    program = models.CharField(unique=True, max_length=64, blank=True, null=True)
    priority = models.CharField(max_length=8, blank=True, null=True)
    program_tech_drivers = models.CharField(max_length=1024, blank=True, null=True)
    si_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    si_probability = models.CharField(max_length=8, blank=True, null=True)
    si_impact = models.CharField(max_length=8, blank=True, null=True)
    si_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    emc_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    emc_probability = models.CharField(max_length=8, blank=True, null=True)
    emc_impact = models.CharField(max_length=8, blank=True, null=True)
    emc_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    power_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    power_probability = models.CharField(max_length=8, blank=True, null=True)
    power_impact = models.CharField(max_length=8, blank=True, null=True)
    power_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    compliance_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    compliance_probability = models.CharField(max_length=8, blank=True, null=True)
    compliance_impact = models.CharField(max_length=8, blank=True, null=True)
    compliance_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    thermal_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    thermal_probability = models.CharField(max_length=8, blank=True, null=True)
    thermal_impact = models.CharField(max_length=8, blank=True, null=True)
    thermal_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    mech_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    mech_probability = models.CharField(max_length=8, blank=True, null=True)
    mech_impact = models.CharField(max_length=8, blank=True, null=True)
    mech_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    pcb_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    pcb_probability = models.CharField(max_length=8, blank=True, null=True)
    pcb_impact = models.CharField(max_length=8, blank=True, null=True)
    pcb_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    lab_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    lab_probability = models.CharField(max_length=8, blank=True, null=True)
    lab_impact = models.CharField(max_length=8, blank=True, null=True)
    lab_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'programs'


class ProjectClasses(models.Model):
    project_class_id = models.AutoField(primary_key=True)
    project_class = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_classes'


class ProjectNotes(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=800, blank=True, null=True)
    links = models.CharField(max_length=256, blank=True, null=True)
    note_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_notes'


class ProjectStages(models.Model):
    stage_id = models.AutoField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    stage_number = models.IntegerField(blank=True, null=True)
    stage_description = models.CharField(max_length=300, blank=True, null=True)
    stage_comments = models.CharField(max_length=1024, blank=True, null=True)
    hw_geo = models.CharField(max_length=40, blank=True, null=True)
    es_engagement = models.DateField(blank=True, null=True)
    power_on_date = models.DateField(blank=True, null=True)
    hw_dev_complete = models.DateField(blank=True, null=True)
    frs = models.DateField(blank=True, null=True)
    new_board_number = models.IntegerField(blank=True, null=True)
    new_board_fru_number = models.IntegerField(blank=True, null=True)
    new_leveraged = models.CharField(max_length=40, blank=True, null=True)
    new_ps_number = models.IntegerField(blank=True, null=True)
    new_chassis_number = models.IntegerField(blank=True, null=True)
    emc_proto1_delivery_date = models.DateField(blank=True, null=True)
    emc_proto1_actual_date = models.DateField(blank=True, null=True)
    emc_proto1_ready_date = models.DateField(blank=True, null=True)
    emc_proto2_delivery_date = models.DateField(blank=True, null=True)
    emc_proto2_actual_date = models.DateField(blank=True, null=True)
    emc_proto2_ready_date = models.DateField(blank=True, null=True)
    emc_protofinal_delivery_date = models.DateField(blank=True, null=True)
    emc_protofinal_actual_date = models.DateField(blank=True, null=True)
    emc_protofinal_ready_date = models.DateField(blank=True, null=True)
    nebs = models.CharField(max_length=40, blank=True, null=True)
    class_b = models.CharField(max_length=40, blank=True, null=True)
    homologation_certs_beyond_tier_1 = models.CharField(max_length=40, blank=True, null=True)
    interface_types = models.CharField(max_length=60, blank=True, null=True)
    number_of_protos_required_by_es = models.CharField(max_length=200, blank=True, null=True)
    si_rules_date = models.DateField(blank=True, null=True)
    si_rules_complete = models.IntegerField(blank=True, null=True)
    power_budget_date = models.DateField(blank=True, null=True)
    power_budget_progress = models.CharField(max_length=40, blank=True, null=True)
    thermal_analysis_date = models.DateField(blank=True, null=True)
    thermal_analysis_progress = models.CharField(max_length=40, blank=True, null=True)
    proto_1_progress_power = models.CharField(max_length=40, blank=True, null=True)
    proto_1_progress_compliance = models.CharField(max_length=40, blank=True, null=True)
    proto_1_progress_emc = models.CharField(max_length=40, blank=True, null=True)
    power_qual_complete_date = models.DateField(blank=True, null=True)
    power_qual_complete_progress = models.CharField(max_length=40, blank=True, null=True)
    final_proto_progress_compliance = models.CharField(max_length=40, blank=True, null=True)
    final_proto_progress_emc = models.CharField(max_length=40, blank=True, null=True)
    emc_test_date = models.DateField(blank=True, null=True)
    emc_gr1089_date = models.DateField(blank=True, null=True)
    emc_report_date = models.DateField(blank=True, null=True)
    emc_report_link = models.CharField(max_length=80, blank=True, null=True)
    emc_test_progress = models.CharField(max_length=40, blank=True, null=True)
    safety_test_date = models.DateField(blank=True, null=True)
    safety_test_progress = models.CharField(max_length=40, blank=True, null=True)
    telcom_test_date = models.DateField(blank=True, null=True)
    telcom_test_progress = models.CharField(max_length=40, blank=True, null=True)
    nebs_hw_available = models.CharField(max_length=40, blank=True, null=True)
    nebs_hw_progress = models.CharField(max_length=40, blank=True, null=True)
    nebs_test_date = models.DateField(blank=True, null=True)
    nebs_test_progress = models.CharField(max_length=40, blank=True, null=True)
    si_comment = models.CharField(max_length=200, blank=True, null=True)
    power_comment = models.CharField(max_length=80, blank=True, null=True)
    emc_comment = models.CharField(max_length=400, blank=True, null=True)
    compliance_comment = models.CharField(max_length=200, blank=True, null=True)
    thermal_comment = models.CharField(max_length=60, blank=True, null=True)
    emc_final_proto = models.CharField(max_length=40, blank=True, null=True)
    compliance_final_proto = models.CharField(max_length=40, blank=True, null=True)
    oxm = models.CharField(max_length=40, blank=True, null=True)
    odm_type = models.CharField(max_length=40, blank=True, null=True)
    pilot_eco_release = models.DateField(blank=True, null=True)
    pilot_eco_prev_date = models.DateField(blank=True, null=True)
    pilot_complete = models.DateField(blank=True, null=True)
    pilot_comp_prev_date = models.DateField(blank=True, null=True)
    production_eco = models.DateField(blank=True, null=True)
    production_eco_progress = models.CharField(max_length=40, blank=True, null=True)
    production_eco_prev_date = models.DateField(blank=True, null=True)
    project_status = models.CharField(max_length=40, blank=True, null=True)
    si_prev_date = models.DateField(blank=True, null=True)
    therm_prev_date = models.DateField(blank=True, null=True)
    pwr_prev_date = models.DateField(blank=True, null=True)
    pwr_chg_date = models.DateField(blank=True, null=True)
    pwr_reason = models.CharField(max_length=40, blank=True, null=True)
    proto_1_prev_date = models.DateField(blank=True, null=True)
    final_proto_prev_date = models.DateField(blank=True, null=True)
    final_proto_reason = models.CharField(max_length=40, blank=True, null=True)
    final_proto_comment = models.CharField(max_length=40, blank=True, null=True)
    emc_prev_date = models.DateField(blank=True, null=True)
    emc_chg_date = models.DateField(blank=True, null=True)
    emc_reason = models.CharField(max_length=40, blank=True, null=True)
    safety_prev_date = models.DateField(blank=True, null=True)
    safety_chg_date = models.DateField(blank=True, null=True)
    safety_reason = models.CharField(max_length=40, blank=True, null=True)
    telcom_prev_date = models.DateField(blank=True, null=True)
    nebs_hw_prev_date = models.DateField(blank=True, null=True)
    nebs_hw_chg_date = models.DateField(blank=True, null=True)
    nebs_prev_date = models.DateField(blank=True, null=True)
    nebs_chg_date = models.DateField(blank=True, null=True)
    nebs_reason = models.CharField(max_length=40, blank=True, null=True)
    pilot_eco_date = models.DateField(blank=True, null=True)
    p0_exit_date = models.DateField(blank=True, null=True)
    p1_exit_date = models.DateField(blank=True, null=True)
    p2_exit_date = models.DateField(blank=True, null=True)
    p3_exit_date = models.DateField(blank=True, null=True)
    p1_replan_exit_date = models.DateField(blank=True, null=True)
    p4_exit_date = models.DateField(blank=True, null=True)
    eco_release_chg_date = models.DateField(blank=True, null=True)
    eco_release_reason = models.CharField(max_length=40, blank=True, null=True)
    frs_change_date = models.DateField(blank=True, null=True)
    proj_status_ryg = models.CharField(max_length=40, blank=True, null=True)
    proj_status_ryg_prev = models.CharField(max_length=8, blank=True, null=True)
    proj_status_change_date = models.DateField(blank=True, null=True)
    si_rules_comment = models.CharField(max_length=40, blank=True, null=True)
    pwr_budget_comment = models.CharField(max_length=40, blank=True, null=True)
    thermal_analysis_comment = models.CharField(max_length=40, blank=True, null=True)
    proto_1_delivery_comment = models.CharField(max_length=40, blank=True, null=True)
    power_qual_comment = models.CharField(max_length=40, blank=True, null=True)
    emc_pscomment = models.CharField(max_length=40, blank=True, null=True)
    safety_internal_test_date = models.DateField(blank=True, null=True)
    safety_internal_test_prev_date = models.DateField(blank=True, null=True)
    safety_internal_test_chg_date = models.DateField(blank=True, null=True)
    safety_internal_test_reason = models.CharField(max_length=40, blank=True, null=True)
    safety_internal_test_comment = models.CharField(max_length=40, blank=True, null=True)
    eco_release_comment = models.CharField(max_length=40, blank=True, null=True)
    frs_comment = models.CharField(max_length=40, blank=True, null=True)
    nebs_hw_avail_comment = models.CharField(max_length=40, blank=True, null=True)
    nebs_cert_comment = models.CharField(max_length=40, blank=True, null=True)
    si_rules_ryg = models.CharField(max_length=40, blank=True, null=True)
    pwr_budget_ryg = models.CharField(max_length=40, blank=True, null=True)
    thermal_analysis_ryg = models.CharField(max_length=40, blank=True, null=True)
    proto_1_delivery_ryg = models.CharField(max_length=40, blank=True, null=True)
    power_qual_chg_date = models.DateField(blank=True, null=True)
    power_qual_prev_date = models.DateField(blank=True, null=True)
    power_qual_reason = models.CharField(max_length=40, blank=True, null=True)
    power_qual_ryg = models.CharField(max_length=40, blank=True, null=True)
    emc_prescan_ryg = models.CharField(max_length=40, blank=True, null=True)
    safety_internal_test_ryg = models.CharField(max_length=40, blank=True, null=True)
    final_proto_ryg = models.CharField(max_length=40, blank=True, null=True)
    pilot_eco_progress = models.CharField(max_length=40, blank=True, null=True)
    pilot_eco_ryg = models.CharField(max_length=40, blank=True, null=True)
    pilot_eco_comment = models.CharField(max_length=40, blank=True, null=True)
    pilot_complete_ryg = models.CharField(max_length=40, blank=True, null=True)
    pilot_complete_comment = models.CharField(max_length=40, blank=True, null=True)
    emc_cert_ryg = models.CharField(max_length=40, blank=True, null=True)
    system_safety_cert_ryg = models.CharField(max_length=40, blank=True, null=True)
    p4_exit_ryg = models.CharField(max_length=40, blank=True, null=True)
    eco_release_ryg = models.CharField(max_length=40, blank=True, null=True)
    frs_ryg = models.CharField(max_length=40, blank=True, null=True)
    nebs_hw_ryg = models.CharField(max_length=40, blank=True, null=True)
    nebs_cert_ryg = models.CharField(max_length=40, blank=True, null=True)
    telecom_chg_date = models.DateField(blank=True, null=True)
    telecom_reason = models.CharField(max_length=40, blank=True, null=True)
    telecom_ryg = models.CharField(max_length=40, blank=True, null=True)
    telecom_comment = models.CharField(max_length=40, blank=True, null=True)
    frs_prev_date = models.DateField(blank=True, null=True)
    frs_progress = models.CharField(max_length=40, blank=True, null=True)
    proto_1_compliance = models.DateField(blank=True, null=True)
    proto_1_compliance_prev_date = models.DateField(blank=True, null=True)
    proto_1_compliance_comment = models.CharField(max_length=80, blank=True, null=True)
    proto_1_emc = models.DateField(blank=True, null=True)
    proto_1_emc_prev_date = models.DateField(blank=True, null=True)
    proto_1_emc_comment = models.CharField(max_length=80, blank=True, null=True)
    final_proto_compliance = models.DateField(blank=True, null=True)
    final_proto_compliance_comment = models.CharField(max_length=40, blank=True, null=True)
    proto_final_emc_date = models.DateField(blank=True, null=True)
    final_proto_emc_comment = models.CharField(max_length=80, blank=True, null=True)
    safety_comment = models.CharField(max_length=80, blank=True, null=True)
    pilot_complete_progress = models.CharField(max_length=40, blank=True, null=True)
    final_proto_compliance_prev_date = models.DateField(blank=True, null=True)
    model = models.CharField(max_length=40, blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_stages'


class ProjectTypes(models.Model):
    project_type_id = models.AutoField(primary_key=True)
    project_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_types'


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project = models.CharField(max_length=80, blank=True, null=True)
    project_type_id = models.IntegerField(blank=True, null=True)
    bu_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    project_class_id = models.IntegerField(blank=True, null=True)
    finance_group_id = models.IntegerField(blank=True, null=True)
    previous_status = models.CharField(max_length=1, blank=True, null=True)
    current_status = models.CharField(max_length=1, blank=True, null=True)
    action = models.CharField(max_length=5, blank=True, null=True)
    project_status_summary = models.CharField(max_length=256, blank=True, null=True)
    changed = models.DateField(blank=True, null=True)
    scope = models.CharField(max_length=40, blank=True, null=True)
    oem = models.CharField(max_length=20, blank=True, null=True)
    odm = models.CharField(max_length=11, blank=True, null=True)
    odm_vendor = models.CharField(max_length=40, blank=True, null=True)
    prj_hw_geo = models.CharField(max_length=10, blank=True, null=True)
    level = models.CharField(max_length=20, blank=True, null=True)
    component = models.CharField(max_length=40, blank=True, null=True)
    rohs = models.CharField(max_length=128, blank=True, null=True)
    vendor = models.CharField(max_length=40, blank=True, null=True)
    frs = models.DateField(blank=True, null=True)
    rev = models.IntegerField(blank=True, null=True)
    rev_date = models.DateField(blank=True, null=True)
    rev_reason = models.CharField(max_length=80, blank=True, null=True)
    project_description = models.CharField(max_length=300, blank=True, null=True)
    next_milestone = models.CharField(max_length=200, blank=True, null=True)
    next_milestone_date = models.DateField(blank=True, null=True)
    doc_link = models.CharField(max_length=128, blank=True, null=True)
    sheet_id = models.CharField(max_length=32, blank=True, null=True)
    checklist_sheet_id = models.CharField(max_length=32, blank=True, null=True)
    rfi_sheet_id = models.CharField(max_length=32, blank=True, null=True)
    sku_sheet_id = models.CharField(max_length=32, blank=True, null=True)
    power_issues_sheet_id = models.CharField(max_length=32, blank=True, null=True)
    power_shipments_sheet_id = models.CharField(max_length=32, blank=True, null=True)
    milestone_link = models.CharField(max_length=128, blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    phase = models.CharField(max_length=40, blank=True, null=True)
    active = models.CharField(max_length=40, blank=True, null=True)
    st_pgm = models.CharField(max_length=24, blank=True, null=True)
    st_rep = models.CharField(max_length=24, blank=True, null=True)
    st_eng_lead = models.CharField(max_length=24, blank=True, null=True)
    st_power_contact = models.CharField(max_length=32, blank=True, null=True)
    st_mechanical_contact = models.CharField(max_length=32, blank=True, null=True)
    st_thermal_contact = models.CharField(max_length=32, blank=True, null=True)
    st_emc_contact = models.CharField(max_length=32, blank=True, null=True)
    st_safety_contact = models.CharField(max_length=32, blank=True, null=True)
    st_nebs_contact = models.CharField(db_column='st_NEBS_contact', max_length=32, blank=True, null=True)  # Field name made lowercase.
    st_pcb_contact = models.CharField(max_length=32, blank=True, null=True)
    tech_drivers = models.CharField(max_length=300, blank=True, null=True)
    si_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    si_probability = models.CharField(max_length=8, blank=True, null=True)
    si_impact = models.CharField(max_length=8, blank=True, null=True)
    si_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    emc_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    emc_probability = models.CharField(max_length=8, blank=True, null=True)
    emc_impact = models.CharField(max_length=8, blank=True, null=True)
    emc_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    power_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    power_probability = models.CharField(max_length=8, blank=True, null=True)
    power_impact = models.CharField(max_length=8, blank=True, null=True)
    power_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    compliance_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    compliance_probability = models.CharField(max_length=8, blank=True, null=True)
    compliance_impact = models.CharField(max_length=8, blank=True, null=True)
    compliance_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    thermal_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    thermal_probability = models.CharField(max_length=8, blank=True, null=True)
    thermal_impact = models.CharField(max_length=8, blank=True, null=True)
    thermal_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    mech_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    mech_probability = models.CharField(max_length=8, blank=True, null=True)
    mech_impact = models.CharField(max_length=8, blank=True, null=True)
    mech_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    pcb_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    pcb_probability = models.CharField(max_length=8, blank=True, null=True)
    pcb_impact = models.CharField(max_length=8, blank=True, null=True)
    pcb_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    lab_technical_assessment = models.CharField(max_length=1024, blank=True, null=True)
    lab_probability = models.CharField(max_length=8, blank=True, null=True)
    lab_impact = models.CharField(max_length=8, blank=True, null=True)
    lab_mitigations = models.CharField(max_length=1024, blank=True, null=True)
    power_control = models.CharField(max_length=40, blank=True, null=True)
    power_monitoring = models.CharField(max_length=40, blank=True, null=True)
    power_scaling_features = models.CharField(max_length=40, blank=True, null=True)
    wattage = models.CharField(max_length=40, blank=True, null=True)
    power_conversion_efficiency = models.CharField(max_length=409, blank=True, null=True)
    bu_priority = models.IntegerField(db_column='BU_Priority', blank=True, null=True)  # Field name made lowercase.
    out_of_scope = models.CharField(max_length=1, blank=True, null=True)
    npi_program_manager = models.CharField(max_length=40, blank=True, null=True)
    npi_hw_lead = models.CharField(max_length=40, blank=True, null=True)
    npi_plm = models.CharField(max_length=40, blank=True, null=True)
    project_id_number = models.IntegerField(blank=True, null=True)
    ecr = models.CharField(db_column='ECR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prjcode = models.CharField(max_length=20, blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class Prototypes(models.Model):
    prototype_id = models.AutoField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    function_id = models.IntegerField(blank=True, null=True)
    subfunction = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    proto1_quantity = models.IntegerField(blank=True, null=True)
    proto2_quantity = models.IntegerField(blank=True, null=True)
    proto3_quantity = models.IntegerField(blank=True, null=True)
    pilot_quantity = models.IntegerField(blank=True, null=True)
    production_quantity = models.IntegerField(blank=True, null=True)
    to_be_returned = models.CharField(max_length=30, blank=True, null=True)
    use_duration = models.CharField(max_length=30, blank=True, null=True)
    comments = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prototypes'


class PurchaseOrders(models.Model):
    po_id = models.AutoField(primary_key=True)
    po_number = models.CharField(max_length=11, blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    pr_number = models.CharField(max_length=11, blank=True, null=True)
    pr_date = models.DateField(blank=True, null=True)
    function_id = models.IntegerField(blank=True, null=True)
    transaction_id = models.IntegerField()
    account_number = models.IntegerField(blank=True, null=True)
    dept_number = models.IntegerField(blank=True, null=True)
    project_code = models.IntegerField(blank=True, null=True)
    vendor_name = models.CharField(max_length=40, blank=True, null=True)
    requestor = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase_orders'


class QuarterlyTransactions(models.Model):
    quarter = models.CharField(db_column='Quarter', max_length=4, blank=True, null=True)  # Field name made lowercase.
    function = models.CharField(db_column='Function', max_length=13, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=14, blank=True, null=True)  # Field name made lowercase.
    bg = models.CharField(db_column='BG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    bu = models.CharField(db_column='BU', max_length=9, blank=True, null=True)  # Field name made lowercase.
    project = models.CharField(db_column='Project', max_length=40, blank=True, null=True)  # Field name made lowercase.
    transaction = models.CharField(db_column='Transaction', max_length=120, blank=True, null=True)  # Field name made lowercase.
    budget = models.DecimalField(db_column='Budget', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    plan = models.DecimalField(db_column='Plan', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    request = models.DecimalField(db_column='Request', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    request_date = models.DateField(db_column='Request_Date', blank=True, null=True)  # Field name made lowercase.
    rollup = models.DecimalField(db_column='Rollup', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    actual = models.DecimalField(db_column='Actual', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    accrued = models.DecimalField(db_column='Accrued', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pending = models.DecimalField(db_column='Pending', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    todays_req = models.DecimalField(db_column='Todays_Req', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    approved = models.DateField(db_column='Approved', blank=True, null=True)  # Field name made lowercase.
    es_plan_chg = models.DecimalField(db_column='ES_Plan_Chg', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    npi_sched_chg = models.DecimalField(db_column='NPI_Sched_Chg', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_scope_chg = models.DecimalField(db_column='Total_Scope_Chg', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    npi_scope_chg = models.DecimalField(db_column='NPI_Scope_Chg', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    oos_proj_totals = models.DecimalField(db_column='OOS_Proj_Totals', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    condition = models.CharField(db_column='Condition', max_length=14, blank=True, null=True)  # Field name made lowercase.
    rts = models.CharField(db_column='RTS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quarterly_transactions'


class Quarters(models.Model):
    quarter_id = models.AutoField(primary_key=True)
    quarter = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quarters'


class Resources(models.Model):
    resource_id = models.AutoField(primary_key=True)
    resource = models.CharField(max_length=80, blank=True, null=True)
    geo_id = models.IntegerField(blank=True, null=True)
    function_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resources'


class RfiRevisions(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    rev_date = models.DateField(blank=True, null=True)
    rev_author = models.CharField(max_length=20, blank=True, null=True)
    rev_description = models.CharField(max_length=480, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rfi_revisions'


class Smartsheet(models.Model):
    entry_type = models.CharField(max_length=32)
    sheetid = models.CharField(max_length=32)
    sheetname = models.CharField(max_length=64, blank=True, null=True)
    milestone = models.CharField(max_length=64, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    need_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    link = models.CharField(max_length=128, blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'smartsheet'


class Targets(models.Model):
    function_id = models.IntegerField(blank=True, null=True)
    project_type_id = models.IntegerField(blank=True, null=True)
    bu_id = models.IntegerField(blank=True, null=True)
    labor_type_id = models.IntegerField(blank=True, null=True)
    quarter = models.CharField(max_length=4, blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'targets'


class Tbh(models.Model):
    function_id = models.IntegerField(blank=True, null=True)
    labor_type_id = models.IntegerField(blank=True, null=True)
    quarter = models.CharField(max_length=4, blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbh'
        unique_together = (('function_id', 'labor_type_id', 'quarter'),)


class Tmp(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField(blank=True, null=True)
    resource_id = models.IntegerField(blank=True, null=True)
    activity = models.CharField(max_length=500, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp'


class TransactionCommentsPipeline(models.Model):
    id = models.IntegerField()
    transaction_entry_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_comments_pipeline'


class TransactionEntries(models.Model):
    transaction_id = models.IntegerField(blank=True, null=True)
    subcategory = models.CharField(max_length=200, blank=True, null=True)
    reason = models.CharField(max_length=40, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    comments = models.CharField(max_length=80, blank=True, null=True)
    quarter = models.CharField(max_length=4, blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transaction_entries'
        unique_together = (('transaction_id', 'subcategory', 'reason', 'author', 'entry_date', 'comments', 'quarter', 'amount'),)


class TransactionFields(models.Model):
    transaction_id = models.IntegerField()
    req_date = models.DateField(blank=True, null=True)
    bu_approved = models.DateField(blank=True, null=True)
    es_approved = models.DateField(blank=True, null=True)
    quarter = models.CharField(max_length=4)
    p1_exit_approved = models.DecimalField(db_column='P1 exit approved', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    planned = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    requested = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    forecasted = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    forecast_comment = models.CharField(max_length=100, blank=True, null=True)
    forecast_change_date = models.DateTimeField(blank=True, null=True)
    forecast_change_user = models.CharField(max_length=64, blank=True, null=True)
    forecast_previous = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    forecast_new = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    not_invoiced = models.CharField(max_length=10, blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transaction_fields'


class TransactionIdsPipeline(models.Model):
    id = models.IntegerField()
    transaction_id = models.IntegerField(unique=True, blank=True, null=True)
    row_id = models.CharField(max_length=50, blank=True, null=True)
    row_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_ids_pipeline'


class TransactionPipeline(models.Model):
    message = models.CharField(max_length=45, blank=True, null=True)
    lstentrydate = models.DateTimeField(db_column='lstEntryDate', blank=True, null=True)  # Field name made lowercase.
    script_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_pipeline'


class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=14)
    transaction = models.CharField(max_length=300, blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    function_id = models.IntegerField(blank=True, null=True)
    subfunction = models.CharField(max_length=20, blank=True, null=True)
    labor_type_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    bu_comment = models.CharField(max_length=200, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class UserBu(models.Model):
    userid = models.CharField(db_column='userId', max_length=12)  # Field name made lowercase.
    bu = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bu'


class UserLoginInfoOld(models.Model):
    userid = models.CharField(db_column='userId', unique=True, max_length=50)  # Field name made lowercase.
    givenname = models.CharField(db_column='givenName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(max_length=20, blank=True, null=True)
    bu = models.CharField(max_length=12, blank=True, null=True)
    lastlogin = models.DateTimeField(db_column='lastLogin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_login_info_old'
        unique_together = (('id', 'userid'),)


class Users(models.Model):
    userid = models.CharField(db_column='userId', unique=True, max_length=50)  # Field name made lowercase.
    userpass = models.CharField(max_length=32, blank=True, null=True)
    givenname = models.CharField(db_column='givenName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(max_length=20, blank=True, null=True)
    bu = models.CharField(max_length=12, blank=True, null=True)
    lastlogin = models.DateTimeField(db_column='lastLogin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('id', 'userid'),)


class Vendors(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'vendors'
