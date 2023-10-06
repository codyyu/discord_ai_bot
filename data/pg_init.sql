CREATE TABLE guilds
(
    id              bigint not null,
    member_count    bigint not null,
    created_at      timestamp,
    installed_at    timestamp,
    status          text not null
);
create unique index guilds_id_uindex
    on guilds (id);