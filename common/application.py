class Routes:
    base_url = "https://reqres.in{}"
    create_user = base_url.format("/api/users")
    get_users_list = base_url.format("/api/users?page=2")
    get_single_user = base_url.format("/api/users/{id}")
    user_not_found = base_url.format("/api/users/23")
    delete_user = base_url.format("/api/users/2")
    update_user = base_url.format("/api/users/{id}")
    login_user = base_url.format("/api/login")
    register_user = base_url.format("/api/register")
