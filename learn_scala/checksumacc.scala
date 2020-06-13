class ChecksumAccumulator{
	private var sum = 0
	def add(b: Byte) : Unit = {
		b = 1
		sum += b
	}
	def checksum() : Int = ~ (sum & 0xFF) + 1
}