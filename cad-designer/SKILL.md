---
name: cad-designer
description: Thiết kế và kiểm định bản vẽ Autodesk AutoCAD đa ngành: cơ khí, kiến trúc, kết cấu, điện, MEP, hạ tầng; chuyển yêu cầu thành đặc tả, tiêu chuẩn dự án, bản vẽ và kiểm thử kỹ thuật.
version: 3.0.0
category: engineering-cad
---

# CAD DESIGNER — Multidiscipline Design & QA v2.0

## 1. Vai trò

Skill này quyết định **vẽ cái gì, theo quy tắc nào, kiểm tra thế nào**; `cad-automation` quyết định **thực thi bằng AutoCAD như thế nào**. Không coi việc tạo được DWG là chứng nhận tính đúng kỹ thuật. Các quyết định liên quan kết cấu chịu lực, an toàn điện, PCCC, cơ khí chịu tải, địa kỹ thuật, giao thông, áp lực hoặc quy chuẩn pháp lý cần người có chuyên môn phê duyệt.

## 2. Quy trình bắt buộc

1. **Phân loại ngành**: mechanical, architectural, structural, electrical, MEP, civil, plant, general.
2. **Phân loại đầu ra**: sơ đồ ý tưởng, bản vẽ tham khảo, bản vẽ thiết kế, shop drawing, as-built, bản vẽ gia công, lắp ráp, sơ đồ nguyên lý, phối hợp bộ môn.
3. **Thu thập yêu cầu**: mục tiêu, đơn vị, hệ tọa độ, kích thước, tiêu chuẩn quốc gia và phiên bản, bản mẫu DWT/DWG, khổ giấy, tỉ lệ, nguồn dữ liệu, yêu cầu xuất file.
4. **Đánh dấu thiếu thông tin**: `BLOCKING` (không thể thiết kế an toàn), `ASSUMPTION` (giả định cho bản minh họa), `OPTIONAL`.
5. **Lập đặc tả hình học**: đối tượng, kích thước, ràng buộc, vị trí, layer, annotation, view, sheet, tolerance và mức độ kiểm chứng.
6. **Bàn giao spec cho `cad-automation`**; không gửi mô tả mơ hồ như “vẽ cho đẹp”.
7. **QA nhiều tầng**: dữ liệu → hình học → trình bày → review kỹ thuật; không dùng hình ảnh để thay thế đo lường.
8. **Bàn giao**: file, preview, danh sách assumption, checklist PASS/FAIL/NOT_CHECKED, điểm cần kỹ sư xác nhận.

## 3. Nguyên tắc tiêu chuẩn

- Chỉ áp dụng tiêu chuẩn **được người dùng chỉ định** hoặc tiêu chuẩn dự án xác minh được. Không gắn nhãn “đạt TCVN/ISO/ASME/IEC/NFPA” nếu chưa kiểm tra đúng số hiệu, năm ban hành, phạm vi và điều khoản.
- Các tài liệu tham khảo thường gặp: ISO 128 (quy tắc thể hiện bản vẽ), ISO 129 (kích thước), ISO 5455 (tỉ lệ), ISO 5457 (khổ giấy), ISO 7200 (khung tên), ISO 1101 (GD&T), ISO 2768 (dung sai chung trong phạm vi áp dụng), ISO 19650 (quản lý thông tin BIM); IEC/IEEE/NFPA và TCVN/QCVN phù hợp cho điện/xây dựng. **Không tự mặc định các bộ này là tiêu chuẩn bắt buộc hoặc bản mới nhất.**
- Nếu người dùng ở Việt Nam và không nêu chuẩn, đề xuất TCVN/QCVN phù hợp **để xác nhận**, không tự tuyên bố tuân thủ.
- Một dự án có thể sử dụng nhiều hệ tiêu chuẩn; phải ghi rõ precedence khi mâu thuẫn.

## 4. Hệ tọa độ, đơn vị, tỉ lệ

- Model Space vẽ đúng kích thước thực theo **đơn vị dự án** (mm/m/inch/feet); xác minh `INSUNITS`, hệ tọa độ, datum và đơn vị chú thích. Không tự chuyển đổi hệ mét/imperial khi chưa được phép.
- WCS là hệ tọa độ toàn cục, UCS có thể là yêu cầu chính đáng cho chi tiết nghiêng, mặt cắt và workflow 3D; không ép tất cả về WCS mà không kiểm tra phép biến đổi.
- Công trình hạ tầng/địa chính: hỏi hệ tọa độ địa lý, mốc cao độ, projection, tọa độ gốc, hướng Bắc, đơn vị cao độ.
- Paper Space: khổ giấy thực, viewport với scale rõ ràng, kiểm tra annotation scale và tỷ lệ PDF.
- Khổ A0 841×1189, A1 594×841, A2 420×594, A3 297×420, A4 210×297 mm là kích thước danh nghĩa ISO A; orientation và lề/khung tên theo tiêu chuẩn áp dụng, không có lề cố định dùng cho mọi dự án.
- Tỉ lệ thường gặp: 1:1, 1:2, 1:5, 1:10, 1:20, 1:50, 1:100; chỉ chọn khi phù hợp ngành, kích thước và khổ giấy.

## 5. Layer, nét vẽ, chữ và block

**Layer schema gợi ý, không phải quy chuẩn quốc gia:**

| Ngành | Layer ví dụ | Ý nghĩa |
|---|---|---|
| Cơ khí | M-OUTLINE, M-CENTER, M-HIDDEN, M-DIM | Biên dạng, tâm, nét khuất, kích thước |
| Kiến trúc | A-WALL, A-DOOR, A-WINDOW, A-TEXT | Tường, cửa, cửa sổ, chữ |
| Kết cấu | S-COLUMN, S-BEAM, S-REBAR, S-DIM | Cột, dầm, thép, kích thước |
| Điện | E-EQUIP, E-CABLE, E-LIGHT, E-TAG | Thiết bị, dây, đèn, nhãn |
| MEP | M-DUCT, P-PIPE, F-FIRE, M-ANNO | Ống gió, ống nước, PCCC, chú thích |
| Hạ tầng | C-ROAD, C-ALIGN, C-LEVEL, C-DRAIN | Đường, tuyến, cao độ, thoát nước |

- Ưu tiên ByLayer cho màu/nét/lineweight; ngoại lệ cần có lý do.
- Không xem bảng màu ACI cố định là “quốc gia quy định”; màu thường là quy ước nội bộ hoặc CTB/STB.
- Layer `0` có thể dùng trong block để kế thừa thuộc tính và có thể có entity trong bản vẽ tùy chuẩn; không xóa hay cấm tuyệt đối.
- Linetype phải được nạp và kiểm tra; centerline/hidden phải đúng scale khi in.
- Khung tên nên dùng attribute block hoặc template dự án, có revision, drawing no., scale, units, date, author, reviewer, status.
- Kiểm tra font Unicode/SHX/BigFont, kích thước chữ **trên bản in**, text orientation, chữ đè nét và thiếu ký tự.

## 6. Ghi kích thước, dung sai và ký hiệu

- Phân biệt **kích thước điều khiển** (driving), **kích thước tham khảo** (reference), **kích thước đo thực** (measured) và text annotation.
- Không tự làm tròn thay đổi ý nghĩa; quy tắc số lẻ và dung sai phải theo dự án.
- Tránh lặp kích thước điều khiển và chuỗi kích thước khép kín không có chủ đích; nhưng kích thước tham khảo/kiểm tra có thể hợp lệ khi được đánh dấu.
- Không ghi kích thước đến đường khuất khi có thể biểu diễn rõ hơn bằng mặt cắt; có ngoại lệ theo tiêu chuẩn và yêu cầu trình bày.
- Với cơ khí, GD&T phải có datum, feature control frame, ký hiệu đúng và phiên bản chuẩn; không dùng ký tự Unicode gần giống thay cho ký hiệu kiểm soát chính thức.
- Dung sai lắp ghép (H7/g6...), độ nhám, nhiệt luyện, mối hàn, độ phẳng... chỉ ghi khi có cơ sở thiết kế.
- Kiểm tra giá trị hiển thị so với geometry và đơn vị; `TextOverride` có thể che giá trị sai nên phải báo nếu dùng.

## 7. Hướng dẫn theo lĩnh vực

### 7.1 Cơ khí, chi tiết máy, khuôn, đồ gá

Yêu cầu tối thiểu: chức năng chi tiết, vật liệu, hình học và kích thước chính, mặt chuẩn, hình chiếu/mặt cắt cần thiết, ren/lỗ, bề mặt làm việc, dung sai chức năng, yêu cầu nhiệt luyện/gia công (nếu đã xác định), mã chi tiết và phiên bản. Với bản lắp: BOM, balloon, lắp ghép, khoảng hở, hướng lắp, chi tiết tiêu chuẩn. Với khuôn dập: phôi, chiều dày, vật liệu, lực dập, khe hở, áp lực tâm, hành trình, an toàn máy; **không tự lấy 5–8% chiều dày làm khe hở chuẩn cho mọi vật liệu**. Nếu thiếu dữ liệu, chỉ vẽ sơ đồ nguyên lý và gắn nhãn KHÔNG DÙNG GIA CÔNG.

**QA:** biên dạng kín, độ đồng tâm, kích thước lỗ, va chạm, vị trí chốt/bu lông, khe hở, đường phân khuôn, số lượng chi tiết, tolerance stack-up khi cần.

### 7.2 Kiến trúc

Yêu cầu: mặt bằng tầng, trục định vị, cao độ, tường, cửa, thang, kích thước thông thủy, tên phòng, hướng Bắc, mặt đứng/mặt cắt, vật liệu, ký hiệu, diện tích, khung tên. Không tự khẳng định tuân thủ thoát nạn, tiếp cận, PCCC, khoảng lùi hoặc mật độ nếu thiếu dữ liệu quy chuẩn và phê duyệt.

**QA:** cửa va tường, cầu thang và cao độ không nhất quán, kích thước thiếu, tên phòng trùng, thiếu trục/cao độ, đối chiếu mặt bằng–mặt đứng–mặt cắt.

### 7.3 Kết cấu

Yêu cầu: hệ trục, mốc cao độ, sơ đồ chịu lực, tiết diện cấu kiện, vật liệu/cấp bền, tải trọng và tổ hợp tải, chi tiết liên kết, thép/cốt thép, lớp bảo vệ, bảng thống kê và tiêu chuẩn tính toán. **Không tự suy ra kích thước cột/dầm/móng để thi công** nếu thiếu tính toán kỹ sư.

**QA:** trục, cao độ, giao cắt, vị trí dầm–cột, cover, neo/nối thép, số lượng và ký hiệu thép, tương thích với kiến trúc/MEP.

### 7.4 Điện và điều khiển

Phân biệt sơ đồ nguyên lý, single-line, wiring, panel layout, cable schedule, grounding, lighting layout. Cần nguồn, điện áp, dòng thiết kế, bảo vệ, loại dây/cáp, tiết diện, terminal, thiết bị và tag. Không tự khẳng định cỡ dây, CB, khả năng cắt, khoảng cách an toàn hay phân vùng nguy hiểm đạt chuẩn.

**QA:** kết nối hở, short logic, tag trùng, số terminal, tham chiếu chéo, cáp/thiết bị không có mã, thông số chưa xác minh.

### 7.5 MEP, HVAC, cấp thoát nước, PCCC

Yêu cầu: mặt bằng, tuyến ống, đường kính/tiết diện, cao độ, độ dốc, thiết bị, van/phụ kiện, insulation, bảo trì, hệ thống ký hiệu, schedule. Kích thước ống và thiết bị phải xuất phát từ tính toán hoặc tài liệu thiết kế.

**QA:** clash với kết cấu, cao độ, độ dốc và chiều chảy, khoảng bảo trì, nhãn, tính liên tục mạng, phối hợp giữa các bộ môn.

### 7.6 Hạ tầng, giao thông, san nền, thoát nước

Yêu cầu: hệ tọa độ, mốc cao độ, alignment, chainage, mặt cắt dọc/ngang, độ dốc, taluy, đường đỏ, hố ga, cống, mạng lưới, bảng khối lượng. Không dùng khoảng cách phẳng thay cho khoảng cách trắc địa nếu sai hệ chiếu.

**QA:** tính liên tục tim tuyến, cao độ, hướng dốc, trùng/đứt tuyến, khối lượng và đơn vị, tương thích dữ liệu khảo sát.

### 7.7 Bản vẽ đa ngành

Đặt hệ tọa độ và datum chung, file xref/đường dẫn chuẩn, tên layer/discipline, mốc cao độ và revision. Phát hiện clash, thay đổi phiên bản, trùng thiết bị, mất xref; không tự kết luận “clash-free” nếu chỉ xem một ảnh 2D.

## 8. Đặc tả bản vẽ chuyển cho CAD Automation

```json
{
  "discipline": "mechanical",
  "purpose": "concept_only",
  "units": "mm",
  "coordinate_system": "WCS",
  "geometry": [
    {"id":"outline","type":"closed_polyline","vertices":[[0,0],[100,0],[100,60],[0,60]],"layer":"M-OUTLINE"},
    {"id":"hole1","type":"circle","center":[50,30],"radius":10,"layer":"M-OUTLINE"}
  ],
  "constraints": [
    {"type":"distance","from":"outline.xmin","to":"outline.xmax","value":100,"tolerance":0.01},
    {"type":"diameter","target":"hole1","value":20,"tolerance":0.01}
  ],
  "annotation": {"dimension_style":"PROJECT_DEFINED","dimensions":["100","60","diameter 20"]},
  "sheet": {"format":"A3","orientation":"landscape","scale":"1:1"},
  "assumptions": ["Ví dụ minh họa; không có vật liệu/dung sai gia công"],
  "approval_required": true
}
```

Chỉ định các ràng buộc **có thể đo được**; đối tượng phải có ID duy nhất. Nếu không đủ thông số, chuyển sang `concept_only` và thêm watermark/ghi chú bản vẽ. Không tự biến sơ đồ ý tưởng thành bản vẽ chế tạo.

## 9. QA có ngưỡng kiểm tra

| Cấp | Nội dung | Bằng chứng |
|---|---|---|
| L0 | đủ thông tin, đơn vị, tiêu chuẩn, scope | spec và assumption log |
| L1 | script/API/file tạo được | execution log, file exists |
| L2 | loại/số lượng đối tượng và layer | inventory JSON |
| L3 | kích thước, tâm, bán kính, diện tích, quan hệ, topology, tọa độ, text–geometry consistency | measured vs expected + epsilon |
| L4 | sheet, text overlap, font, lineweight, clipping, khung tên, preview PDF | hình ảnh/PDF được review |
| L5 | rà soát tính đúng thiết kế và pháp lý theo ngành | chữ ký hoặc biên bản phê duyệt của chuyên gia |

**Nguyên tắc:** L4 không phải “gần như chắc chắn đúng”; ảnh có thể bỏ sót kích thước sai hoặc vấn đề an toàn. L5 không được giả lập bằng AI. Nếu thiếu chứng cứ, đánh dấu `NOT_CHECKED`, không tự nâng thành PASS.

### Kiểm tra hình học phổ quát

- Đơn vị và phép chuyển hệ tọa độ; kiểm tra scale bản in.
- Entity rỗng, duplicate, self-intersection, polyline không kín, vùng có diện tích âm/zero, kích thước âm.
- Giao nhau trái phép, sai độ song song/vuông góc/đồng tâm, lỗ vượt mép, trùng lắp annotation.
- Dims đo thực khác giá trị hiển thị; rounding làm sai dung sai.
- Xref thiếu, block/tag trùng, font missing, plot style missing, object nằm ngoài khung.
- Ngưỡng epsilon phải theo đơn vị, độ chính xác thiết kế và đặc tính; không áp dụng một epsilon cố định cho toàn bộ ngành.

### Ví dụ báo cáo QA

```json
{
  "drawing": "demo_plate.dwg",
  "status": "NEEDS_REVIEW",
  "checks": [
    {"id":"GEO-001","level":"L3","name":"width","expected":100,"measured":100,"tolerance":0.01,"status":"PASS"},
    {"id":"GEO-002","level":"L3","name":"hole diameter","expected":20,"measured":20,"tolerance":0.01,"status":"PASS"},
    {"id":"VIS-001","level":"L4","name":"PDF visual inspection","status":"NOT_CHECKED"},
    {"id":"ENG-001","level":"L5","name":"engineer sign-off","status":"NOT_CHECKED"}
  ]
}
```

## 10. Vòng lặp thiết kế – kiểm thử – sửa

1. Chạy validation, gom lỗi theo nhóm: input / geometry / layer / dimension / sheet / technical.
2. Ưu tiên sửa sai kích thước, tọa độ, liên kết trước khi chỉnh thẩm mỹ.
3. Tái chạy test đã lỗi và regression tests liên quan; giữ log các lần sửa.
4. Giới hạn vòng lặp tự động theo cấu hình dự án (mặc định 3), sau đó yêu cầu con người kiểm tra. Không tự lặp vô hạn.
5. Nếu gặp lỗi COM, gửi cho `cad-automation` xử lý ở tầng thực thi; không yêu cầu AI đoán lệnh để thoát prompt.
6. Khi có mâu thuẫn tiêu chuẩn hoặc yêu cầu kỹ thuật, dừng và hỏi người dùng/chuyên gia thay vì tự chọn ngẫu nhiên.

## 11. Hướng dẫn phản hồi cho AI local

- Ưu tiên tiếng Việt rõ ràng, thuật ngữ CAD chính xác; cung cấp JSON spec ngắn trước khi code.
- Chỉ hỏi các thông số `BLOCKING` thực sự cần; với bản minh họa có thể dùng giả định và ghi rõ.
- Không tự gắn nhãn “chuẩn ISO/TCVN” khi chưa có tiêu chuẩn, phiên bản và checklist điều khoản.
- Khi user nói “vẽ AutoCAD”, xác định: muốn code, DXF, DWG đã tạo, hay hướng dẫn thao tác. Không báo có file DWG nếu chưa chạy AutoCAD và kiểm tra đường dẫn.
- Nếu user yêu cầu sửa DWG, yêu cầu file hoặc đường dẫn và backup; không tự thay bản gốc.
- Khi xuất bản vẽ, tóm tắt: nội dung, đơn vị, kích thước chính, sheets, file output, PASS/FAIL/NOT_CHECKED, assumption và yêu cầu phê duyệt.

## 12. Checklist bàn giao

- [ ] Mục đích và ngành được xác định.
- [ ] Đơn vị, hệ tọa độ, datum được xác minh.
- [ ] Tiêu chuẩn dự án và phiên bản được xác định hoặc ghi `UNSPECIFIED`.
- [ ] Geometry và ràng buộc có giá trị kỳ vọng.
- [ ] Layer/linetype/text/dim/block nhất quán.
- [ ] Đủ hình chiếu/mặt cắt/sơ đồ theo mục đích.
- [ ] Không thiếu thông số bắt buộc cho mức độ đầu ra.
- [ ] L1/L2/L3 có bằng chứng, L4 được review hoặc ghi NOT_CHECKED.
- [ ] PDF được kiểm tra khổ giấy, tỉ lệ, font và nét.
- [ ] File gốc được bảo toàn, backup và revision rõ ràng.
- [ ] Người có chuyên môn xác nhận khi bản vẽ dùng thi công/gia công/an toàn.

## 13. Ghi chú nguồn và thay đổi so với v1.1.0

Kế thừa `cad-designer` v1.1.0: khổ giấy, tỉ lệ, layer, dimension, blocks, DWT, plotting, template đa ngành, QA L1–L4 và vòng lặp thiết kế. Đã loại bỏ quy tắc quá tuyệt đối về mm, WCS, layer 0, kích thước chữ, màu “quốc gia”, purge/audit bắt buộc; phân biệt tiêu chuẩn tham khảo và tiêu chuẩn dự án; bổ sung kiến trúc, kết cấu, điện, MEP, hạ tầng, giao diện spec có thể kiểm tra, L5 review kỹ thuật và an toàn. Đây là tài liệu quy trình, không phải chứng nhận tuân thủ tiêu chuẩn hoặc kiểm thử trực tiếp trên AutoCAD.

## 20. Vietnam TCVN/QCVN Professional Router v3.0 — BẮT BUỘC

Đọc `../standards/registry.json` và `../standards/INDUSTRY_PROFILES.md` trước khi lập bản vẽ cho dự án Việt Nam. Đây là registry định tuyến, không phải toàn văn tiêu chuẩn. Không áp dụng tiêu chuẩn của ngành khác chỉ vì có số hiệu tương tự. Nếu thiếu phiên bản, điều khoản hoặc văn bản gốc, trạng thái là `NOT_CHECKED` hoặc `MANUAL_REVIEW`, tuyệt đối không ghi `TCVN PASS`.

### 20.1 Chọn tiêu chuẩn theo từng ngành
1. **Cơ khí:** phân biệt chi tiết, lắp ráp, khuôn, gia công tấm, đường ống công nghệ; xác định hệ hình chiếu, dung sai, nhám, vật liệu, kiểm tra chain dimensions và BOM. Chỉ kiểm tra quy tắc GD&T sau khi có nguồn và datum.
2. **Kiến trúc:** xác định loại công trình, cấp công trình, giai đoạn thiết kế, chiều cao, số tầng, công năng, yêu cầu tiếp cận, PCCC, phối hợp với kết cấu/MEP. Không tự chốt kích thước lối thoát nạn từ ghi nhớ.
3. **Kết cấu:** phân biệt bản vẽ thể hiện cốt thép với hồ sơ tính toán chịu lực. Tải trọng, cốt thép, cấu tạo và liên kết là `MANUAL_REVIEW` nếu chưa có kết quả tính toán và văn bản quy phạm chính xác.
4. **Điện:** chọn đúng phần/năm của TCVN 7447 và hệ thống điện áp; đánh số thiết bị, cáp, mạch, tủ, sơ đồ một sợi. Bảo vệ điện, tiết diện cáp, nối đất cần tính toán và kiểm duyệt.
5. **MEP:** HVAC, cấp thoát nước, phòng cháy và đường ống công nghệ có tiêu chuẩn khác nhau. Xác minh thông số thiết bị, lưu lượng, độ dốc, cao độ và không gian bảo trì; kiểm tra clash là hình học, không thay thế thẩm định.
6. **Hạ tầng:** lấy hệ tọa độ/mốc cao độ từ dữ liệu dự án, không giả định VN-2000 là đủ để chuyển đổi tọa độ; kiểm tra lý trình, độ dốc, trắc dọc, trắc ngang và phạm vi hành lang.

### 20.2 Đầu ra hợp đồng tiêu chuẩn
Tạo `standards_manifest.json` theo `../examples/standards_manifest.example.json` gồm số hiệu, năm, nguồn, phạm vi, điều khoản được kiểm, chứng cứ, phương pháp, kết quả. Các rule chỉ từ registry đều là `CATALOG_VERIFIED`, không được báo đạt điều khoản.

### 20.3 Trình tự kiểm định
(1) xác minh chuẩn và phạm vi; (2) kiểm dữ liệu đầu vào; (3) hình học/dimensions; (4) layer/lineweight/linetype/text; (5) layout/viewport/plot; (6) đối chiếu điều khoản có toàn văn; (7) người duyệt. Lỗi không xác định phải ghi rõ `NOT_CHECKED`, không tự đổi thành PASS.

### 20.4 Chính sách chất lượng
Chỉ ghi `READY_FOR_ENGINEER_REVIEW` khi tất cả kiểm thử tự động bắt buộc PASS và không còn lỗi BLOCKING. Chỉ người được ủy quyền mới có thể xác nhận `APPROVED_FOR_CONSTRUCTION` hoặc `APPROVED_FOR_MANUFACTURE`.
