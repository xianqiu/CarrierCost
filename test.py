from carriercost import CostCalculator, Package


if __name__ == '__main__':
    cc = CostCalculator('jd-a.cpf', 'jd-a.table')
    package = Package()
    package.set_box(1, 1, 1, 3)
    package.set_departure(dep_city='东莞')
    package.set_destination(des_city='临沧市')
    print(cc.get_cost(package))




