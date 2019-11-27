select 
b.nome as bairro,
count(*) as qtda
from bairro_bairro as b
inner join indicacao_indicacao as i on i.assunto like CONCAT('%', b.nome, '%')
group by b.nome
order by qtda desc