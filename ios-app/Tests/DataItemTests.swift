import XCTest
@testable import MyApp

final class DataItemTests: XCTestCase {
    
    func testDataItemInitialization() {
        // Given
        let title = "Test Task"
        let description = "Test Description"
        
        // When
        let dataItem = DataItem(title: title, description: description)
        
        // Then
        XCTAssertEqual(dataItem.title, title)
        XCTAssertEqual(dataItem.description, description)
        XCTAssertEqual(dataItem.status, .pending)
        XCTAssertFalse(dataItem.isProcessing)
        XCTAssertNotNil(dataItem.id)
    }
    
    func testDataItemWithCustomStatus() {
        // Given
        let title = "Processing Task"
        let description = "Task in progress"
        let status = ProcessingStatus.processing
        
        // When
        let dataItem = DataItem(
            title: title,
            description: description,
            status: status,
            isProcessing: true
        )
        
        // Then
        XCTAssertEqual(dataItem.title, title)
        XCTAssertEqual(dataItem.description, description)
        XCTAssertEqual(dataItem.status, status)
        XCTAssertTrue(dataItem.isProcessing)
    }
    
    func testProcessingStatusDisplayName() {
        // Test all status display names
        XCTAssertEqual(ProcessingStatus.pending.displayName, "Pending")
        XCTAssertEqual(ProcessingStatus.processing.displayName, "Processing")
        XCTAssertEqual(ProcessingStatus.completed.displayName, "Completed")
        XCTAssertEqual(ProcessingStatus.failed.displayName, "Failed")
    }
    
    func testProcessingStatusSystemImage() {
        // Test all status system images
        XCTAssertEqual(ProcessingStatus.pending.systemImage, "clock")
        XCTAssertEqual(ProcessingStatus.processing.systemImage, "gear")
        XCTAssertEqual(ProcessingStatus.completed.systemImage, "checkmark.circle.fill")
        XCTAssertEqual(ProcessingStatus.failed.systemImage, "xmark.circle.fill")
    }
    
    func testSampleData() {
        // Given & When
        let sampleData = DataItem.sampleData
        
        // Then
        XCTAssertEqual(sampleData.count, 3)
        XCTAssertEqual(sampleData[0].status, .completed)
        XCTAssertEqual(sampleData[1].status, .processing)
        XCTAssertEqual(sampleData[2].status, .pending)
        XCTAssertTrue(sampleData[1].isProcessing)
        XCTAssertFalse(sampleData[0].isProcessing)
        XCTAssertFalse(sampleData[2].isProcessing)
    }
    
    func testDataItemCodable() throws {
        // Given
        let originalItem = DataItem(
            title: "Codable Test",
            description: "Testing JSON encoding/decoding",
            timestamp: Date(),
            status: .completed
        )
        
        // When - Encode
        let encoder = JSONEncoder()
        encoder.dateEncodingStrategy = .iso8601
        let jsonData = try encoder.encode(originalItem)
        
        // Then - Decode
        let decoder = JSONDecoder()
        decoder.dateDecodingStrategy = .iso8601
        let decodedItem = try decoder.decode(DataItem.self, from: jsonData)
        
        // Verify
        XCTAssertEqual(originalItem.id, decodedItem.id)
        XCTAssertEqual(originalItem.title, decodedItem.title)
        XCTAssertEqual(originalItem.description, decodedItem.description)
        XCTAssertEqual(originalItem.status, decodedItem.status)
        XCTAssertEqual(originalItem.isProcessing, decodedItem.isProcessing)
    }
}
