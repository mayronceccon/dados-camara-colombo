select 
b.nome as bairro,
CONCAT(v.nome, ' (', v.apelido, ')') as vereador,
count(*) as qtda
from bairro_bairro as b
inner join indicacao_indicacao as i on i.assunto like CONCAT('%', b.nome, '%')
inner join vereador_vereador as v on v.id = i.vereador_id
group by b.nome, i.vereador_id
order by qtda desc