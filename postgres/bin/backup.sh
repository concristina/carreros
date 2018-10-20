#!/usr/bin/env bash


### Create a database backup.
###
### Usage:
###     $ docker-compose (exec |run --rm) db backup.sh


set -o errexit
set -o pipefail
set -o nounset


working_dir="$(dirname ${0})"
source "${working_dir}/_sourced/constants.sh"
source "${working_dir}/_sourced/messages.sh"


message_welcome "Backing up the '${DB_NAME}' database..."


if [[ "${DB_USER}" == "postgres" ]]; then
    message_error "Backing up as 'postgres' user is not supported. Assign 'DB_USER' env with another one and try again."
    exit 1
fi

export PGHOST="${DB_SERVICE}"
export PGPORT="${DB_PORT}"
export PGUSER="${DB_USER}"
export PGPASSWORD="${DB_PASS}"
export PGDATABASE="${DB_NAME}"

backup_filename="${BACKUP_FILE_PREFIX}_$(date +'%Y_%m_%dT%H_%M_%S').sql.gz"
pg_dump | gzip > "/backups/${backup_filename}"


message_success "'${DB_NAME}' database backup '${backup_filename}' has been created and placed in '/backups'."