from corpus import adverbial_modifiers
from commands import command

adverb = adverbial_modifiers.adv_eventually
cmd = command.PreCmdEventually(adverb)
print(cmd.cmd_neg_adv)
print(cmd.cmd_dic_adv)



