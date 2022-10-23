import desafiolunarapi.repository as rep


def test_create():

    mining = {
        "name": "Campo nome alterado",
        "description": "Descrição alterada",
    }

    rep.create(mining)

    filtered_mining = {k: v for k, v in rep.all()[-1].items()
                       if k in ['name', 'description']}

    assert mining == filtered_mining


def test_find_by_id(): assert rep.find_by_id(1) != None


def test_all(): assert rep.all() != None


def test_edit():

    id = 1

    mining = {
        "name": "Campo nome alterado",
        "description": "Descrição alterada",
    }

    rep.edit(id, mining)

    assert mining["description"] == [item["description"]
                                     for item in rep.all() if id == item["id"]][-1]


def test_remove():

    id = 1

    rep.remove(id)

    assert rep.find_by_id(id) == None
