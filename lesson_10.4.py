class Gadget:   # brand, model, year

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


def gadget_info(self):
    return f"I have {self.brand} {self.model} and it is from {self.year} "


class Phone(Gadget):  # applications-> list, contacts ->list , settings -> dict

    def __init__(self, brand, model, year, applications, contacts, settings):
        super().__init__(brand, model, year)
        self.applications = applications
        self.contacts = contacts
        self.settings = settings.list

    def add_app(self, app):
        if app not in self.applications:
            self.applications.append(app)

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)

    def del_contact(self, del_contact):
        self.contacts.remove(del_contact)

    def edit_settings(self,  **settings):
        self.settings.update(settings)


class Computer(Gadget):     #OS, applications

    def __init__(self, brand, model, year, applications, os):
        super().__init__(brand, model, year)
        self.OS = os
        self.applications = applications
        self.trash = []
        print(f"IT`s computer {self.brand} {self.model} from {self.year}. "
              f"It has {self.applications} and {self.OS} on it.")


    def add_app(self, app):
        if app not in self.applications:
            self.applications.append(app)

    def del_app(self, del_app):
        self.trash.append(del_app)
        self.applications.remove(del_app)

    def explore_trash(self):
        print(self.trash)

    def remove_trash(self):
        self.trash.clear()


class TV(Gadget):        # settings
    def __init__(self, brand, model, year, channel_list, **settings):
        super().__init__(brand, model, year)
        self.settings = settings
        self.channel_list = channel_list


    def add_channel(self, channel):
        if channel not in self.channel_list:
            self.channel_list.append(channel)

    def del_channel(self, del_channel):
        self.channel_list.remove(del_channel)

    def edit_settings(self, **settings):
        self.settings.update(settings)


#p1 = Phone('Motorolla', 'V360', 2007, ['WWP', 'MsWord'], ['Vasya, 555-777-99'], 'power' = 500)
c1 = Computer('Asus', 'A65897', 2018, ['youtube'], 'Linux')
#tv1 = TV('Panasonic', '65sddds', 2019, ['ut1', 'Hromadske'], ['color' = 'blue', 'contrast' = 84)]


