insert into core_region (id, name, name_en)
values  (1, 'Tây Bắc Bộ', 'Northwest'),
        (2, 'Đông Bắc Bộ', 'Northeast'),
        (3, 'Đồng bằng sông Hồng', 'Red River Delta'),
        (4, 'Bắc Trung Bộ', 'North Central Coast'),
        (5, 'Nam Trung Bộ', 'South Central Coast'),
        (6, 'Tây Nguyên', 'Central Highlands'),
        (7, 'Đông Nam Bộ', 'Southeast'),
        (8, 'Đồng bằng sông Cửu Long', 'Mekong River Delta');
insert into core_province (id, name, region_id, type)
values  (1, 'Hà Nội', 3, 'C'),
        (2, 'Hà Giang', 2, 'P'),
        (4, 'Cao Bằng', 2, 'P'),
        (6, 'Bắc Kạn', 2, 'P'),
        (30, 'Hải Dương', 3, 'P'),
        (10, 'Lào Cai', 1, 'P');
insert into core_district (id, name, type, province_id)
values  (1, 'Ba Đình', 'UD', 1),
        (2, 'Hoàn Kiếm', 'UD', 1),
        (3, 'Tây Hồ', 'UD', 1),
        (24, 'Hà Giang', 'C', 2),
        (26, 'Đồng Văn', 'RD', 2),
        (27, 'Mèo Vạc', 'RD', 2),   
        (64, 'Chợ Đồn', 'RD', 6),
        (65, 'Chợ Mới', 'RD', 6),     
        (86, 'Bảo Thắng', 'RD', 10),
        (87, 'Bảo Yên', 'RD', 10);                
insert into core_ward (id, name, type, district_id)
values  (1, 'Phúc Xá', 'W', 1),
        (4, 'Trúc Bạch', 'W', 1);