# CAD Skills Pro v3.0 — Vietnam TCVN/QCVN Edition

Hai SKILL.md tương thích vai trò: `cad-designer` phân loại tiêu chuẩn và thiết kế; `cad-automation` thực thi AutoCAD. Thư mục `standards/` cung cấp registry có nguồn; `tools/` có preflight DXF không phá hủy; `examples/` có manifest mẫu.

## Cài đặt
Giải nén và giữ nguyên cấu trúc. Nếu hệ thống skill chỉ nhận từng thư mục, chép `cad-designer/` và `cad-automation/` vào skill root, đồng thời chép `standards/`, `tools/`, `examples/` vào cùng cấp. Kiểm tra đường dẫn tương đối; sửa đường dẫn nếu harness yêu cầu. Cài `ezdxf` nếu dùng validator. Để điều khiển AutoCAD cần Python trên Windows, `pywin32`, AutoCAD desktop phù hợp và quyền chạy lệnh trên máy đó. Skill không tự tạo quyền truy cập máy.

## Cảnh báo tuân thủ
Danh mục chuẩn được đối chiếu từ nguồn công khai tại thời điểm tạo; **chưa tích hợp toàn văn có bản quyền của TCVN** và chưa có bộ kiểm định điều khoản đầy đủ. Không tuyên bố bản vẽ `đạt TCVN` chỉ dựa vào các skill này. Phải bổ sung văn bản hợp pháp, rule mapping, DWT được phê duyệt và nghiệm thu kỹ sư. QCVN cần kiểm tra văn bản sửa đổi, hiệu lực và phạm vi áp dụng tại ngày dự án.

## Test nhanh
`python tools/validate_dxf.py example.dxf --out report.json`

## Nguồn catalog
VSQI: https://tieuchuan.vsqi.gov.vn/ ; văn bản pháp luật: https://vanban.chinhphu.vn/
