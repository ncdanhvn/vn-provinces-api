insert into core_region (id, name, name_en)
values  (1, 'Tây Bắc Bộ', 'Northwest'),
        (2, 'Đông Bắc Bộ', 'Northeast'),
        (3, 'Đồng bằng sông Hồng', 'Red River Delta'),
        (4, 'Bắc Trung Bộ', 'North Central Coast'),
        (5, 'Nam Trung Bộ', 'South Central Coast'),
        (6, 'Tây Nguyên', 'Central Highlands'),
        (7, 'Đông Nam Bộ', 'Southeast'),
        (8, 'Đồng bằng sông Cửu Long', 'Mekong River Delta');
insert into core_province (id, name, region_id, type, area, population)
values  (1, 'Hà Nội', 3, 'C', 3359.82, 8330830),
        (2, 'Hà Giang', 2, 'P', 7927.55, 887090),
        (4, 'Cao Bằng', 2, 'P', 6700.39, 542220),
        (6, 'Bắc Kạn', 2, 'P', 4859.96, 323710),
        (8, 'Tuyên Quang', 2, 'P', 5867.95, 801670),
        (10, 'Lào Cai', 1, 'P', 6364.25, 761890);
insert into core_district (id, name, type, province_id, is_border, is_coastal)
values  (1, 'Ba Đình', 'UD', 1, 0, 0),
        (2, 'Hoàn Kiếm', 'UD', 1, 0, 0),
        (3, 'Tây Hồ', 'UD', 1, 0, 0),
        (24, 'Hà Giang', 'C', 2, 0, 0),
        (26, 'Đồng Văn', 'RD', 2, 1, 0),
        (27, 'Mèo Vạc', 'RD', 2, 1, 0),
        (64, 'Chợ Đồn', 'RD', 6, 0, 1),
        (65, 'Chợ Mới', 'RD', 6, 0, 1),  
        (86, 'Bảo Thắng', 'RD', 10, 1, 1),
        (87, 'Bảo Yên', 'RD', 10, 0, 0);              
insert into core_ward (id, name, type, district_id)
values  (1, 'Phúc Xá', 'W', 1),
        (4, 'Trúc Bạch', 'W', 1);
insert into core_numberplate (id, province_id)
values  (29, 1),
        (30, 1),
        (31, 1),
        (32, 1),
        (23, 2),
        (11, 4),
        (97, 6),
        (22, 8),
        (24, 10);
insert into core_province_neighbours (id, from_province_id, to_province_id)
values  (138, 1, 2),
        (140, 2, 1),
        (142, 1, 4),
        (144, 4, 1),
        (146, 1, 6),
        (148, 6, 1);
        
