import Foundation

struct DataItem: Identifiable, Codable {
    let id: UUID
    let title: String
    let description: String
    let timestamp: Date?
    let status: ProcessingStatus
    let isProcessing: Bool
    
    init(id: UUID = UUID(), title: String, description: String, timestamp: Date? = nil, status: ProcessingStatus = .pending, isProcessing: Bool = false) {
        self.id = id
        self.title = title
        self.description = description
        self.timestamp = timestamp
        self.status = status
        self.isProcessing = isProcessing
    }
}

enum ProcessingStatus: String, Codable, CaseIterable {
    case pending = "pending"
    case processing = "processing"
    case completed = "completed"
    case failed = "failed"
}

extension DataItem {
    static let sampleData: [DataItem] = [
        DataItem(
            title: "Sample Task 1",
            description: "This is a sample task that demonstrates the app functionality",
            timestamp: Date(),
            status: .completed
        ),
        DataItem(
            title: "Processing Task",
            description: "This task is currently being processed by the backend",
            timestamp: Date().addingTimeInterval(-3600),
            status: .processing,
            isProcessing: true
        ),
        DataItem(
            title: "Pending Task",
            description: "This task is waiting to be processed",
            timestamp: Date().addingTimeInterval(-7200),
            status: .pending
        )
    ]
}
