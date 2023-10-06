CREATE TABLE guilds
(
    id              bigint not null,
    member_count    bigint not null,
    created_at      timestamp,
    installed_at    timestamp,
    status          text not null,
    updated_at      timestamp
);
create unique index guilds_id_uindex
    on guilds (id);

CREATE TABLE members
(
    id              bigint not null,
    guild_id        bigint not null,
    name            text,
    display_name    text,
    bot             boolean,
    status          text not null,
    joined_at       timestamp,
    created_at      timestamp,
    updated_at      timestamp
);
create unique index members_id_guild_id_uindex
    on members (id, guild_id);