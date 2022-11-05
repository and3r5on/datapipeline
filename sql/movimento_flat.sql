create table movimento_flat  as
    select  a.nome  as nome_associado,
            a.sobrenome as sobrenome_associado,
            a.idade as idade_associado,
            m.vlr_transacao as vlr_transacao_movimento,
            m.des_transacao as des_transacao_movimento,
            m.data_movimentacao as data_movimento,
            ca.num_cartao as numero_cartao,
            ca.nom_impresso as nome_impresso_cartao,
            c.data_criacao + interval '1 month' as data_criacao_cartao, --1mes depois da conta aberta
            c.tipo as tipo_conta,
            c.data_criacao as data_criacao_conta
    from associado a join conta c on (a.id = c.id_associado)
            join cartao ca on (ca.id_conta=c.id) 
            join movimento m on (m.id_cartao=ca.id)
    order by a.nome;



