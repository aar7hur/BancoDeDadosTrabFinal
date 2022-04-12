

if __name__ == "__main__":

    import argparse
    
    parser = argparse.ArgumentParser(
        description="Ferramenta utilizada para externalizar o acesso"
        "ao banco de dados de forma facilitada através de uma API"
    )
 
    # subparsers will represents all subcommands that this command line is
    # reponsible for
    subparsers = parser.add_subparsers(help="Sub-command help")


    # manager use case is one subcommand of this command line.subparse
    # In the manager use case, we can perform any operation. In this case,
    # each supbarse represents one operation
    parser_get_database = subparsers.add_parser(
        "get_db_info", help=" Use this get informations from database"
    )
    parser_get_database.add_argument("--get_by_user_name")
    parser_get_database.add_argument("--get_all_rented")
    parser_get_database.add_argument("--get_all_not_rented")
    parser_get_database.add_argument("--get_all_cars")
    parser_get_database.add_argument("--get_all_car_model")
    parser_get_database.add_argument("--get_all_car_version") 
    parser_get_database.add_argument("--get_all_user")

    args = parser.parse_args()

    # it is necessary to implement cliMamanger here
    pass