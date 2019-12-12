from .permissions import add_perm, has_perm, perm_exists, remove_perm, set_perm
from .predicates import (Predicate, always_allow, always_deny, always_false,
                         always_true, is_active, is_authenticated,
                         is_group_member, is_staff, is_superuser, predicate)
from .rulesets import (RuleSet, add_rule, remove_rule, rule_exists, set_rule,
                       test_rule)

VERSION = (2, 1, 1, 'final', 1)

default_app_config = 'rules.apps.RulesConfig'
