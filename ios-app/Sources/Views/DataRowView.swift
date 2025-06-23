import SwiftUI

struct DataRowView: View {
    let item: DataItem
    
    var body: some View {
        HStack {
            VStack(alignment: .leading, spacing: 4) {
                Text(item.title)
                    .font(.headline)
                    .foregroundColor(.primary)
                
                Text(item.description)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .lineLimit(2)
                
                if let timestamp = item.timestamp {
                    Text(timestamp, style: .date)
                        .font(.caption)
                        .foregroundColor(.tertiary)
                }
            }
            
            Spacer()
            
            if item.isProcessing {
                ProgressView()
                    .scaleEffect(0.8)
            } else {
                Image(systemName: item.status == .completed ? "checkmark.circle.fill" : "circle")
                    .foregroundColor(item.status == .completed ? .green : .gray)
            }
        }
        .padding(.vertical, 4)
    }
}

struct DataRowView_Previews: PreviewProvider {
    static var previews: some View {
        List {
            DataRowView(item: DataItem.sampleData[0])
            DataRowView(item: DataItem.sampleData[1])
        }
    }
}
