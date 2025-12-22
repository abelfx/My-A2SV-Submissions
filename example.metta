; Basic MeTTa example — asserts some facts and queries
(: Predicate Type)
(: Evaluation Type)

; facts
(fact loves alice bob)
(fact loves bob carol)

; simple query
(result ?x
  (loves alice ?x))
