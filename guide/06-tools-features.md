# Module 06: Tools & Features

**Thời gian đọc:** 15 phút | **Mức độ:** Beginner-Intermediate
**Cập nhật:** 2026-03-01 | Claude Opus 4.6 / Sonnet 4.6

---

Module này là cheat sheet tra cứu nhanh tất cả tính năng của Claude.ai -- từ chọn model đến tools, từ file handling đến integrations.

---

## 6.1 Tổng quan tính năng theo Plan

[Cập nhật 03/2026]

| Tính năng | Free | Pro ($20/th) | Max ($100–200/th) | Team ($25/ng/th) | Enterprise |
|-----------|------|-------------|-------------------|------------------|------------|
| Chat cơ bản | Có | Có | Có | Có | Có |
| Web Search | Có | Có | Có | Có | Có |
| Artifacts | Có | Có | Có | Có | Có |
| Upload files | Có | Có | Có | Có | Có |
| Projects | 5 projects | Không giới hạn | Không giới hạn | + Shared | + Admin |
| File Creation (docx, pptx...) | Có | Có | Có | Có | Có |
| Styles (preset + custom) | Có | Có | Có | Có | Có |
| Memory | Có | Có | Có | Có | Có |
| Extended Thinking | Hạn chế | Có | Có | Có | Có |
| Chọn model | Không | Có | Có + Opus mặc định | Có | Có |
| MCP Connectors | Không | Có | Có | Có | Có |
| Research | Không | Có | Có | Có | Có |
| Dung lượng sử dụng | Thấp | 5x Free | Cao hơn ($100: ~10x, $200: ~20x) | 5x Free | Custom |

**Lưu ý:** Bảng này cập nhật đến 03/2026. Anthropic thường xuyên cập nhật features -- kiểm tra claude.ai cho thông tin mới nhất. Memory hiện có trên Free plan từ Q1/2026. Max plan có 2 tier giá: $100/th và $200/th (dung lượng cao hơn).

---

## 6.2 Chọn Model

[Cập nhật 02/2026]

| Model | Điểm mạnh | Khi nào dùng | Tốc độ |
|-------|----------|-------------|--------|
| **Claude Opus 4.6** | Suy luận sâu nhất, Extended thinking | Debug phức tạp, phân tích multi-system, kiến trúc hệ thống | Chậm nhất |
| **Claude Sonnet 4.6** | Cân bằng tốc độ và chất lượng, Extended thinking, 1M context (beta) | Công việc hàng ngày, viết tài liệu, code review | Trung bình |
| **Claude Haiku 4.5** | Nhanh nhất, chi phí thấp | Q&A nhanh, tra cứu, task đơn giản | Nhanh nhất |

**Cách chọn model:** Click tên model ở đầu conversation > Chọn model muốn dùng.

**Quy tắc chọn nhanh:** Bắt đầu với Sonnet 4.6 cho hầu hết công việc. Chuyển sang Opus 4.6 khi cần suy luận sâu. Dùng Haiku 4.5 cho task nhanh không cần chất lượng cao.

### Context Window

| Model             | Context Window                           | Tương đương                 |
| ----------------- | ---------------------------------------- | --------------------------- |
| Claude Opus 4.6   | 200,000 tokens (chuẩn), 1M tokens (beta) | 500–700 / 2,500–3,500 trang |
| Claude Sonnet 4.6 | 200,000 tokens (chuẩn), 1M tokens (beta) | 500–700 / 2,500–3,500 trang |
| Claude Haiku 4.5  | 200,000 tokens                           | 500–700 trang               |


[Nguồn: Anthropic Docs - Models Overview]

---

## 6.3 Extended Thinking

[Cập nhật 03/2026]

[Nguồn: Anthropic Docs - Extended Thinking]
URL: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking

> **Lưu ý thuật ngữ:**
> - **Extended thinking** = UI toggle trên Claude.ai ("Search and tools" > "Extended thinking") — đây là tính năng bạn dùng hàng ngày
> - **Adaptive Thinking** = API feature riêng biệt (`thinking: {type: "adaptive"}`) — chỉ dành cho developer dùng API trực tiếp, KHÔNG phải tên khác của Extended thinking

Extended thinking cho phép Claude "suy nghĩ sâu hơn" trước khi trả lời. Claude tạo thinking block nội bộ (hiển thị cho bạn xem trên Claude.ai), sau đó đưa ra câu trả lời dựa trên suy luận đó.

### Cách bật

1. Mở conversation
2. Click "Search and tools" dưới ô nhập tin nhắn
3. Toggle **"Extended thinking"** > ON

### Khi nào bật

| Bật | Không cần |
|-----|-----------|
| Debug lỗi phức tạp trên nhiều hệ thống | Hỏi đáp đơn giản, tra cứu nhanh |
| Phân tích root cause từ log SLAM/Lidar | Viết email ngắn, tóm tắt cơ bản |
| Review code có nhiều dependency | Tạo checklist đơn giản |
| So sánh và đánh giá nhiều giải pháp | Dịch thuật, paraphrase |
| Lập kế hoạch multi-step workflow | Format lại tài liệu có sẵn |

### Tips quan trọng

[Nguồn: Anthropic Docs - Extended Thinking Tips]
URL: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips

**Bỏ "think step-by-step".** Khi bật Extended thinking, Claude TỰ ĐỘNG suy luận từng bước. Không cần thêm chain-of-thought instructions -- thực tế, thêm vào có thể làm giảm hiệu quả.

**Đơn giản hóa prompt.** Extended thinking hoạt động tốt nhất với prompt rõ ràng, ít "steering". Để Claude tự quyết định cách suy nghĩ.

**Đọc thinking block.** Claude.ai hiển thị thinking process. Đọc để hiểu Claude đang suy luận thế nào, rồi điều chỉnh prompt nếu cần.

**Chấp nhận response time lâu hơn.** Đó là đánh đổi cho chất lượng cao hơn.

---

## 6.4 Web Search và Research

### Web Search

**Khi nào dùng:** Cần thông tin current (sau training cutoff), verify thông tin, check latest docs.

**Cách bật:** Message input > Click "Search and tools" > Toggle "Web Search". Hoặc prompt: "Search the web for..."

**Lưu ý:** Web Search tốn thêm tokens (search results được add vào context).

### Research

[Nguồn: Anthropic Help Center - Research]
URL: https://support.anthropic.com/en/articles/11088861

**Khi nào dùng:** Cần research sâu với multiple sources, tổng hợp đa nguồn, cần citations.

**Cách bật:** Message input > Click "Search and tools" > Select "Research".

| Aspect | Web Search | Research |
|--------|-----------|---------------|
| Depth | Quick lookup | Deep dive |
| Sources | 1-3 sources | Multiple sources |
| Output | Direct answer | Report có citations |
| Thời gian | Giây | Phút |

---

## 6.5 File Handling

### Upload files trong conversation

[Nguồn: Anthropic Help Center - Uploading Files to Claude]

| Category | Extensions | Max Size |
|----------|-----------|----------|
| Tài liệu | PDF, DOCX, TXT, MD, HTML | 30MB |
| Code | PY, JS, JSON, YAML, XML | 30MB |
| Hình ảnh | PNG, JPG, WEBP, GIF | 30MB |
| Data | CSV, XLSX | 30MB |

**Giới hạn:** Tối đa 20 files per conversation. XLSX yêu cầu bật "Code execution and file creation".

### Tạo files

Claude có thể trực tiếp tạo các loại file:

| Loại | Yêu cầu |
|------|---------|
| Word (.docx) | Bật "Code execution and file creation" |
| Excel (.xlsx) | Bật "Code execution and file creation" |
| PowerPoint (.pptx) | Bật "Code execution and file creation" |
| PDF | Tự động |
| Markdown, Code files | Tự động |

### Paste vs Upload -- Khi nào dùng gì

| Tình huống | Cách tốt nhất | Lý do |
|-----------|---------------|-------|
| Code snippet < 50 dòng | **Paste** trực tiếp | Nhanh, dễ discuss inline |
| Error log < 100 dòng | **Paste** trực tiếp | Claude thấy ngay |
| Full source file | **Upload** file | Giữ structure, line numbers |
| Document cần formatting | **Upload** file | Preserve tables, headers |
| Tài liệu dùng lại nhiều lần | **Project Knowledge** | Không tốn context mỗi chat |

---

## 6.6 Artifacts

Artifacts là output dạng rich content mà Claude tạo ra -- code, documents, diagrams, React components.

**Khi nào Claude tạo Artifact:**

- Code dài (> 15 dòng)
- Documents có formatting
- React components
- Mermaid diagrams
- SVG graphics

**Bạn có thể:** Xem rendered output, copy code, download file, iterate với feedback.

---

## 6.7 MCP Connectors

[Nguồn: Anthropic Help Center - Setting up and using Integrations]

MCP Connectors cho phép Claude truy cập dữ liệu từ dịch vụ bên ngoài.

| Connector | Use case |
|-----------|----------|
| Google Drive | Đọc documents, spreadsheets |
| Slack | Tìm kiếm conversations |
| Gmail | Tham chiếu emails |
| GitHub | Truy cập repositories |
| Notion | Đọc/cập nhật pages |
| Jira | Xem/quản lý tickets |

**Setup:** Settings > Connected Apps > Connect.

**Lưu ý:** Mỗi connector tốn context tokens. Chỉ connect khi thực sự cần. Review quyền truy cập định kỳ.

[Cập nhật 02/2026] Danh sách connectors mở rộng liên tục. Kiểm tra Connected Apps để xem mới nhất.

---

## 6.8 Image Search

Claude có thể tìm kiếm hình ảnh trên web.

**Khi nào dùng:** Minh họa cho tài liệu hoặc presentation. Reference images cho thiết kế. So sánh visual giữa các giải pháp.

**Cách dùng:** Yêu cầu trong prompt: "Tìm hình ảnh về..." hoặc dùng kết hợp với Web Search.

---

## 6.9 Prompt Generator và Prompt Improver

[Nguồn: Anthropic Docs - Prompt Generator & Prompt Improver]
URL (Generator): https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator
URL (Improver): https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver

Hai công cụ trên **Anthropic Console** (console.anthropic.com) -- KHÔNG phải trên Claude.ai chat. Cần Anthropic API account.

### Prompt Generator

Mô tả task bằng ngôn ngữ tự nhiên > Claude tạo prompt hoàn chỉnh với XML tags, variables, best practices.

### Prompt Improver

Paste prompt hiện tại > Claude phân tích điểm yếu và rewrite thành version tối ưu. Các cải thiện: chain-of-thought, XML standardization, example enrichment.

| Tình huống | Dùng gì |
|-----------|---------|
| Bắt đầu task hoàn toàn mới | **Generator** |
| Có prompt nhưng kết quả chưa tốt | **Improver** |
| Migrate prompt từ ChatGPT/Gemini | **Improver** |
| Tạo template cho team dùng chung | **Generator** rồi **Improver** |

---

## 6.10 Structured Outputs

[Nguồn: Anthropic Docs - Structured Outputs]
URL: https://docs.anthropic.com/en/docs/build-with-claude/structured-outputs

Yêu cầu Claude trả về JSON theo schema cụ thể. Chi tiết và ví dụ: xem Module 05, mục 5.7.

**Claude.ai:** Dùng prompt-based với schema trong `<output_format>`. Thêm "CHỈ JSON, không markdown."

**API:** Dùng Structured Outputs API -- guaranteed 100% schema compliance.

---

## 6.11 Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Conversation mới | Ctrl/Cmd + N |
| Tìm kiếm conversations | Ctrl/Cmd + K |
| Focus vào ô nhập tin nhắn | / |

---

## 6.12 Bảng Quyết Định Nhanh: Tôi Cần Gì?

| Tôi muốn... | Dùng tính năng |
|-------------|----------------|
| Hỏi nhanh 1 câu | Chat thường |
| Claude nhớ cách tôi làm việc | Profile Preferences + Memory |
| Làm project dài nhiều ngày | Projects |
| Output ngắn gọn hơn | Style: Concise |
| Viết tài liệu chính thức | Style: Formal + File Creation |
| Claude đọc file tôi upload | File Upload |
| Claude tìm info mới nhất | Web Search |
| Tạo file Word/Excel/PPT | File Creation |
| Code, diagram, interactive content | Artifacts |
| Nghiên cứu chuyên sâu | Research |
| Claude tương tác với Notion/Gmail | MCP Connectors |
| Task cần phân tích sâu | Extended thinking |

---

## 6.13 Bảng tổng hợp tất cả Tools

| Tool | Cách bật | Tốn thêm tokens? | Khi nào dùng |
|------|---------|-------------------|-------------|
| **Web Search** | Search and tools > Web Search | Có | Thông tin current, verify facts |
| **Research** | Search and tools > Research | Có (nhiều) | Research sâu, đa nguồn |
| **Extended thinking** | Search and tools > Extended thinking | Có | Debug phức tạp, suy luận sâu |
| **File Upload** | Nút clip (đính kèm) | Có | Phân tích files |
| **File Creation** | Yêu cầu trong prompt | Settings required | Tạo docx, xlsx, pptx |
| **Artifacts** | Tự động | Có | Code, diagrams, components |
| **MCP Connectors** | Settings > Connected Apps | Có | Truy cập dịch vụ ngoài |
| **Prompt Generator** | console.anthropic.com | Không | Tạo prompt mới |
| **Prompt Improver** | console.anthropic.com | Không | Cải thiện prompt có sẵn |

**Quy tắc chung:** Mỗi tool bật thêm đều tốn context tokens. Chỉ bật khi cần. Tắt khi xong.

---

---

## 6.14 Claude Desktop & Cowork

Ngoài Claude.ai (web), Claude còn có **Claude Desktop** — ứng dụng native cho macOS/Windows với tính năng **Cowork mode**: cho phép Claude thao tác trực tiếp trên file system, tự động nhiều bước, và lên lịch task định kỳ.

| Tính năng Cowork | Mô tả |
|------------------|-------|
| **File access** | Đọc, tạo, sửa files trong thư mục bạn chọn |
| **Global Instructions** | Instructions mặc định cho mọi session |
| **Folder Instructions** | Instructions riêng theo thư mục/project |
| **Scheduled Tasks** | Tự động chạy task theo lịch (daily, weekly...) |
| **Skills** | Mở rộng khả năng chuyên biệt — tạo file, review tài liệu, viết docs có cấu trúc |
| **Plugins** | Đóng gói skills + commands + connectors cho từng role (productivity, PM, data...) |
| **MCP Connectors** | Kết nối với dịch vụ bên ngoài (Notion, Jira, Google Drive, Slack...) |

[Cập nhật 03/2026] Skills là thư mục chứa instructions mà Claude load on-demand cho task chuyên biệt — từ tạo file Word/Excel đến review tài liệu. Plugins đóng gói nhiều skills thành bộ cài đặt theo role. Phân loại chi tiết, danh sách khuyến nghị, và hướng dẫn cài đặt: xem **Module 10, mục 10.6**.

**Yêu cầu:** Pro plan trở lên. Download tại https://claude.ai/download.

**Chi tiết đầy đủ:** Xem **Module 10: Claude Desktop & Cowork**.

---

**Tiếp theo:**

- Module 10: Claude Desktop & Cowork -- hướng dẫn chi tiết Cowork mode
- Module 03: Prompt Engineering -- kỹ thuật viết prompt hiệu quả
- Module 04: Context Management -- quản lý conversation dài
